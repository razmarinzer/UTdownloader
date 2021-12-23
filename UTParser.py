from bs4 import BeautifulSoup as bs
import requests

main_link = 'https://www.youtube.com/'
response = requests.get(main_link + '/c/selfedu_rus/videos')
html = bs(response.text, 'lxml')


video_block = html.find_all()
print(video_block[0].html)


# response = requests.get('https://www.youtube.com/c/selfedu_rus/videos/').text
# html = bs(response, 'lxml')
#
# a = html.find(text='href="/watch?v=7WVYqjdMa6U"')
# print(a)

# elem = html.find_all(attrs={'"href="'})
# print(elem)

# children_a = a.findChildren()
# print(children_a)

# for link in html.find_all('a'):
#     print(link.get('href'))

