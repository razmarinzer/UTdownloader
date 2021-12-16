from bs4 import BeautifulSoup
import requests
import re

def scrape_videos(url):

    req = requests.get(url)
    send = BeautifulSoup(req.text, "html.parser")
    search = send.find_all("script")
    key = '"videoId":'
    data = re.findall(key + r"([^*]{11})", str(search))

    return data


def scrape_lists(url):

    req = requests.get(url)
    send = BeautifulSoup(req.text, "html.parser")
    search = send.find_all("script")
    key = '"playlistID":"'
    data = re.findall(key + r"([^*]{34})", str(search))

    return data

if  __name__ == "__main__":
    url = "https://www.youtube.com/c/selfedu_rus/playlists"
    data = scrape_lists(url)
    data = data[::3]
    data = data[:-2]

    for element in data:
        output = 'https://www.youtube.com/playlist?list=' + element
        vid = scrape_videos(output)
        vid = vid[::3]
        vid = vid[:-1]

        for element in vid:
            with open("E:/Python/Projects/Parse/parse.txt", "a", encoding="utf-8") as files:
                files.write(str('https://www.youtube.com/watch?v=' + element + '\n'))
                print('https://www.youtube.com/watch?v=' + element)