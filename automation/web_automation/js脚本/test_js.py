# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from automation.web_automation.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("guchenli")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(2)
        js ="document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        for code in [
            "return document.title","return JSON.stringify(performance.timing)"
        ]:
            print(self.driver.execute_script(code))
    def test_js_1(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        time.sleep(2)
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        print(self.driver.execute_script('return document.getElementById("train_date").value'))