# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait :
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(3)

    def test_hogarts(self):
        self.driver.get("https://ceshiren.com/")
        #直接等待  //*[@id="ember639"]/a //*[@id="ember639"]
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        time.sleep(5)
        # def wait():
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="category-name"]')) >=1
        # WebDriverWait(self.driver, 10).until(wait)
        # self.driver.find_element(By.XPATH, '//*[@class="category-name""]').click()
    def teardown(self):
        self.driver.quit()
