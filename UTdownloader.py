from lxml import html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

import time

import pytube
import moviepy.editor as mpe

"""Cуть программы: Написать скрипт, который ищет новые видео на youtube на канале selfedu и загружает их в каталог
на локальный компьютер. Новые видео - те, которые еще не были загружены при предыдущих запусках скрипта. Предусмотреть
 запуск скрипта по расписанию. Предусмотреть запись ошибок в текстовый файл или базу данных. Предусмотреть
 дополнительный метод для очистки списка уже загруженных файлов. Хранить список загруженных видео в текстовом
 файле или в базе данных. В будущем можно сделать интерфейс для интерактивной работы. Интерфейс - окно, кнопка
  - прочитать список, читает список всех видео на канале, отмечает уже загруженные. Вторая кнопка “загрузить”
   - загружает видео, отмеченные в списке для загрузки."""


class UTDownloader:

    def __init__(self):
        self.db_controller = DBManager()
        self.parser = Parser('selfedu_rus')
        self.downloader = Downloader()

    def download_all_new(self):
        new_video_refs = self.get_new_video_refs()
        for video_ref in new_video_refs:
            self.downloader.download_video(video_ref)

        return new_video_refs

    def get_new_video_refs(self):
        old_video_refs = self.db_controller.get_old_video_refs()
        all_video_refs = self.parser.get_all_video_refs()

        new_video_refs = [element for element in all_video_refs if element not in old_video_refs]

        new_video_refs = ['https://www.youtube.com/watch?v=bN1xpI6f3Vo']
        return new_video_refs


class Parser:

    def __init__(self, channel, scroll_pause_time=0):
        self.channel = channel
        self._main_link = 'https://www.youtube.com/'
        self._scroll_pause_time = scroll_pause_time or 3

    def get_all_video_refs(self):

        html_text = self._get_html_text()

        root = html.fromstring(html_text)

        elements = root.xpath("//h3[@class='style-scope ytd-grid-video-renderer']/a/@href")

        elements = [self._main_link + el for el in elements]

        return elements

    def _get_html_text(self):
        pass

        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)

        driver.get('{}/c/{}/videos'.format(self._main_link, self.channel))

        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        print('Current height - {}'.format(last_height))
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

            # Wait to load page
            time.sleep(self._scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            print('Current height - {}'.format(new_height))
            if new_height == last_height:
                print("Thats enough")
                break
            last_height = new_height

        html_text = driver.page_source

        driver.close()

        return html_text


class DBManager:

    def get_old_video_refs(self):
        return []


class Downloader:

    def __init__(self, folder=''):
        self.folder = folder or 'Youtube_videos'
        if not os.path.isdir(folder):
            os.mkdir(folder)

        self.title = ''

    def download_video(self, ref, with_higest_res=False, merge_with_audio=False):

        you_video = pytube.YouTube(ref)

        video_streams = you_video.streams.filter(subtype="mp4")

        if not with_higest_res:
            video_streams.filter(progressive=True)

        video_streams.order_by('resolution').desc()

        if not video_streams:
            raise IndexError('Video streams is empty')

        video_stream = video_streams[0]

        audio_stream = None

        if not video_stream.is_progressive:
            audio_streams = you_video.streams.filter(only_audio=True).order_by('abr').desc()

            if not audio_streams:
                raise IndexError('Audio streams is empty')

            audio_stream = audio_streams[0]

        filename = you_video.video_id + ' - ' + you_video.title

        if not video_stream.is_progressive:
            video_stream.download(output_path=self.folder, filename=filename + '.mp4')
        else:
            video_stream.download(output_path=self.folder, filename=filename + ' - video.mp4')
            audio_stream.download(output_path=self.folder, filename=filename + ' - audio.webm')

            if merge_with_audio:
                self.merge_video_audio(you_video.video_id)

    def merge_video_audio(self, video_id):

        file_list = os.listdir(self.folder)

        file_list = [file_name for file_name in file_list if self._get_video_id_from_filename(file_name) == video_id]

        filename_video = ''
        filename_audio = ''
        final_filename = ''
        for filename in file_list:
            namelist = filename.split(' - ')
            if len(namelist) == 3:
                if namelist[2] == 'video.mp4':
                    filename_video = filename
                    final_filename = namelist[0] + namelist[1] + '.mp4'
                elif namelist[2] == 'audio.webm':
                    filename_audio = filename

        if not filename_video:
            raise FileNotFoundError('Video file not found')

        if not filename_audio:
            raise FileNotFoundError('Audio file not found')

        my_clip = mpe.VideoFileClip(filename_video)
        final_audio = mpe.AudioFileClip(filename_audio)

        final_clip = my_clip.set_audio(final_audio)
        final_clip.write_videofile(final_filename)

    @staticmethod
    def _get_resolution_value(resolution_string):
        return int("".join(filter(str.isdigit, resolution_string)))

    @staticmethod
    def _get_video_id_from_filename(filename):
        namelist = filename.split(' - ')
        return namelist[0]

if __name__ == '__main__':
    downloader = UTDownloader()
    result = downloader.download_all_new()

    print(result)



