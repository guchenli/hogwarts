# -*- coding: utf-8 -*-
import os
import time

from selenium import webdriver

class Base:
    def setup(self):
        #方法返回环境变量键的值
        #browser=firefox pytest + 文件名
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def teardown(self):
        time.sleep(3)
        self.driver.quit()
