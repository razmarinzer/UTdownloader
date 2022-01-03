from lxml import html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

"""Cуть программы: Написать скрипт, который ищет новые видео на youtube на канале selfedu и загружает их в каталог
на локальный компьютер. Новые видео - те, которые еще не были загружены при предыдущих запусках скрипта. Предусмотреть
 запуск скрипта по расписанию. Предусмотреть запись ошибок в текстовый файл или базу данных. Предусмотреть
 дополнительный метод для очистки списка уже загруженных файлов. Хранить список загруженных видео в текстовом
 файле или в базе данных. В будущем можно сделать интерфейс для интерактивной работы. Интерфейс - окно, кнопка
  - прочитать список, читает список всех видео на канале, отмечает уже загруженные. Вторая кнопка “загрузить”
   - загружает видео, отмеченные в списке для загрузки."""


class UTdownloader:

    def __init__(self):
        self.db_controller = DBManager()
        self.parser = Parser('selfedu_rus')

    def download_all_new(self):
        new_video_refs = self.get_new_video_refs()
        for video_ref in new_video_refs:
            self.download_video_from_ref(video_ref)

        return new_video_refs

    def get_new_video_refs(self):
        old_video_refs = self.db_controller.get_old_video_refs()
        all_video_refs = self.parser.get_all_video_refs()

        new_video_refs = [element for element in all_video_refs if element not in old_video_refs]
        return new_video_refs

    def download_video_from_ref(self, video_ref):
        pass


class Parser:
    pass

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


if __name__ == '__main__':
    downloader = UTdownloader()
    result = downloader.download_all_new()

    print(result)



