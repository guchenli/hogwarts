# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element(By.ID, "kw")
        el.send_keys("selenium测试")
        el1 = self.driver.find_element(By.ID, "su")
        action = TouchActions(self.driver)
        action.tap(el1)
        action.scroll_from_element(el, 0, 10000).perform()
