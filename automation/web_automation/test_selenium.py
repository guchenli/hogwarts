# -*- coding: utf-8 -*-
import time

import selenium
from selenium import webdriver


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_hogarts(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("热门").click()

    def teardown(self):
        self.driver.quit()
