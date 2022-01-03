from selenium import webdriver


class SeleniumParser(object):

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.go_to_links()

    def go_to_links(self):
        self.driver.get('https://www.youtube.com/c/selfedu_rus/videos')
        tag_a = self.driver.find_elements_by_tag_name('a')
        for links in tag_a:
            print(links.get_attribute('href'))


def main():
    driver = webdriver.Chrome()
    parser = SeleniumParser(driver)
    parser.parse()


if __name__ == "__main__":
    main()