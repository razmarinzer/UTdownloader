from bs4 import BeautifulSoup
import requests
import re

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
        self.parser = Parser()

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

    def __init__(self, url=''):
        self.url = url or 'https://www.youtube.com/c/selfedu_rus/videos'

    def get_all_video_refs(self):

        req = requests.get(self.url)
        send = BeautifulSoup(req.text, "html.parser")
        search = send.find_all("script")
        key = '"videoId":'
        data = re.findall(key + r"([^*]{11})", str(search))
        # print(data)

        return data

    # def scrape_lists(self, url):
    #
    #     req = requests.get(url)
    #     send = BeautifulSoup(req.text, "html.parser")
    #     search = send.find_all("script")
    #     key = '"playlistID":"'
    #     data = re.findall(key + r"([^*]{34})", str(search))
    #
    #     return data


class DBManager:

    def get_old_video_refs(self):
        return []


if __name__ == '__main__':
    downloader = UTdownloader()
    result = downloader.download_all_new()

    print(result)

    # url = "https://www.youtube.com/c/selfedu_rus/playlists"
    # data = scrape_lists(url)
    # data = data[::3]
    # data = data[:-2]
    #
    # for element in data:
    #     output = 'https://www.youtube.com/playlist?list-' + element
    #     vid = scrape_videos(output)
    #     vid = vid[::3]
    #     vid = vid[:-1]
    #
    #     for element in vid:
    #         with open("E:/Python/Projects/Parse/parse.txt", "a", encoding="utf-8") as files:
    #             files.write(str('https://www.youtube.com/watch?v=' + element + '\n'))
    #             print('https://www.youtube.com/watch?v=' + element)

