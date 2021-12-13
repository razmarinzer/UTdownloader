import urllib.request
import json

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

    def download_all_new(self):
        new_video_refs = self.get_new_video_refs()
        for video_ref in new_video_refs:
            self.download_video_from_ref(video_ref)

    def get_new_video_refs(self):
        old_video_refs = self.db_controller.get_old_video_refs()

        return []

    def download_video_from_ref(self, video_ref):
        pass


class Parser:

    def get_all_video_from_channel(channel_id):
        pass

    def get_all_video_with_titles_from_channel(channel_id):
        pass

    def get_information_from_youtube_video(video_id):
        pass

class DBManager:

    def get_old_video_refs(self):
        return []


if __name__ == '__main__':

    # My first commit
    downloader = UTdownloader()
    result = downloader.download_all_new()
