import json
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

douyu = 'http://www.douyu.com'


class RobetUpWeb:
    def __init__(self, cookie_file=None):
        self.cookies = json.loads(open(cookie_file, 'r').read()) if cookie_file is not None else None
        self.browser = webdriver.Chrome()

    def login(self):
        for each in self.cookies:
            self.browser.add_cookie(each)
        self.browser.refresh()
        time.sleep(1)

    def go_to_room(self, room_id):
        website = douyu+'/'+ room_id
        self.browser.get(website)

    def go_to_website(self,website):
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

    def search_in_weibo(self, s):
        search_box=self.browser.find_element_by_class_name('W_input')
        ActionChains(self.browser).move_to_element(search_box).click().perform()
        search_box.send_keys(s)
        search_button=self.browser.find_element_by_class_name('W_ficon')
        ActionChains(self.browser).move_to_element(search_button).click().perform()

    def get_danmu(self):
        danmu_box=self.browser.find_element_by_class_name('c-list')
        latest_danmu=self.browser.find_element_by_class_name('jschartli')
        print(latest_danmu)


if __name__ == "__main__":
    import os
    path=os.path.expanduser('~/IdeaProjects/qb/')
    d=RobetUpWeb(path+'douyu_cookie.txt')

    # d.go_to_website('http://weibo.com')
    # d.login()
    # time.sleep(5)
    # d.login()
    # time.sleep(3)
    # d.login()
    # d.search_in_weibo('just_a_sleep')
    d.browser.get('http://www.douyu.com/t/lck')
    d.login()
    # 关闭弹出来的小页面
    n_close=d.browser.find_element_by_class_name('normallevel-close')
    time.sleep(3)
    ActionChains(d.browser).move_to_element(n_close).click(n_close).perform()
    time.sleep(5)
    d.get_danmu()


    # text_area=browser.find_element_by_class_name('s_ipt')
    # send_button=browser.find_element_by_class_name('s_btn')
    # text_area.send_keys('23333')
    # ActionChains(browser).move_to_element(send_button).click(send_button).perform()
