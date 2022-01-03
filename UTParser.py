
from lxml import html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

SCROLL_PAUSE_TIME = 3

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

main_link = 'https://www.youtube.com/'
driver.get(main_link + '/c/selfedu_rus/videos')

last_height = driver.execute_script("return document.documentElement.scrollHeight")
print('Current height - {}'.format(last_height))
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    print('Current height - {}'.format(new_height))
    if new_height == last_height:
        print("Thats enough")
        break
    last_height = new_height

html_text = driver.page_source

driver.close()

root = html.fromstring(html_text)

elements = root.xpath("//h3[@class='style-scope ytd-grid-video-renderer']/a/@href")

elements = [main_link + el for el in elements]

print(elements)


