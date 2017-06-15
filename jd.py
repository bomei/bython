import json
import threading
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
import arrow



class JD:
    def __init__(self, cookie_file):
        self.cookies = json.loads(open(cookie_file, 'r').read())
        self.browser = webdriver.Chrome()

    def login(self):
        for each in self.cookies:
            self.browser.add_cookie(each)
        self.browser.refresh()
        time.sleep(1)

    def go_to_xiaomi6(self):
        url = 'http://item.jd.com/3312381.html'
        self.browser.get(url)

    def click_choose_btn(self):
        choose_btn = self.browser.find_element_by_id('InitCartUrl')
        ActionChains(self.browser).move_to_element(choose_btn).click(choose_btn).perform()

    def qiang(self):
        while True:
            try:
                self.click_choose_btn()
                time.sleep(0.01)
                if self.browser.current_url != 'http://item.jd.com/3312381.html#none':
                    time.sleep(10000)
                self.browser.refresh()
            except:
                time.sleep(10000)


def single():
    jd = JD('jd.co')

    jd.go_to_xiaomi6()
    time.sleep(3)
    jd.login()
    jd.qiang()


def main():
    for i in range(4):
        t = threading.Thread(target=single)
        t.start()


if __name__ == '__main__':
    last_min = 0
    while True:
        if arrow.now() > arrow.get('2017-06-15 23:59:00+08:00'):
            break

        if arrow.now().datetime.minute != last_min:
            print(arrow.now())
            last_min=arrow.now().datetime.minute
            time.sleep(5)
    main()
