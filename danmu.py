import json
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

douyu = 'http://www.douyu.com'


class Danmu:
    def __init__(self, cookie_file):
        self.cookies = json.loads(open(cookie_file, 'r').read())
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get(douyu)
        for each in self.cookies:
            self.browser.add_cookie(each)
        self.browser.refresh()
        time.sleep(1)

    def go_to_room(self, room_id):
        website = douyu+'/'+ room_id
        self.browser.get(website)

    def send_danmu(self, danmu):

        index_video=self.browser.find_element_by_class_name('cs-textarea')
        print(type(index_video))
        index_video.send_keys(danmu)
        print(index_video)
        time.sleep(3)
        send_button=self.browser.find_element_by_class_name('b-btn')
        ActionChains(self.browser).move_to_element(send_button).click(send_button).perform()
        ActionChains(self.browser).move_to_element(send_button).context_click(send_button).perform()

if __name__ == "__main__":
    d=Danmu('douyu_cookie.txt')

    d.login()

    d.go_to_room('922564')
    n_close=d.browser.find_element_by_class_name('normallevel-close')
    time.sleep(3)
    ActionChains(d.browser).move_to_element(n_close).click(n_close).perform()
    time.sleep(2)
    d.send_danmu('23333')
    time.sleep(10)
    # browser=webdriver.Firefox()
    # browser.get('http://www.baidu.com')
    # text_area=browser.find_element_by_class_name('s_ipt')
    # send_button=browser.find_element_by_class_name('s_btn')
    # text_area.send_keys('23333')
    # ActionChains(browser).move_to_element(send_button).click(send_button).perform()
