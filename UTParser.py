from bs4 import BeautifulSoup as bs
import requests
import re

main_link = 'https://www.youtube.com/'
response = requests.get(main_link + '/c/selfedu_rus/videos')
html = bs(response.text, 'html.parser')

video_blocks = html.find_all('script')

scripts_string = str(video_blocks)

# print(scripts_string)
position = -1
first = True

refs = []

while first or position != -1:
    position = scripts_string.find('videoId":"', position+1)

    c_ref = scripts_string[position+10:position+21]
    if position != -1 and c_ref not in refs:
        refs.append(c_ref)
    first = False


#
# key = '"videoId":'
# data = re.findall(key + r"([^*]{11})", scripts_string)
#
# print(data)

print(len(refs))

for ref in refs:
    print('https://www.youtube.com/watch?v=' + ref)




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

