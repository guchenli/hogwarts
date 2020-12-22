# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from 自动化.web自动化.base import Base


class TestWindows(Base):

    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[1])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys("guchenli")