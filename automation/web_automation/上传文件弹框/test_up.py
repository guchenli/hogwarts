# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from automation.web_automation.base import Base


class TestUp(Base):
    def test_up(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        # send_keys只对input标签有效
        self.driver.find_element(By.ID, 'stfile').send_keys('D:/pythonProject/hogwarts_gcl/automation/web_automation/imagedata/allure.png')
        time.sleep(5)