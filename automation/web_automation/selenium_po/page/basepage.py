# -*- coding: utf-8 -*-


import yaml
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

data_file = "D:/pythonProject/hogwarts_gcl/automation/web_automation/selenium_po/data1.yaml"

class BasePage:
    _base_url = ""

    def __init__(self, _base_url: WebDriver = None):
        # 避免driver重复初始化，第一次初始化的时候，driver是空的，所以走到了
        # if的逻辑
        if _base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = _base_url

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 显示等待方法
    def wait_for_click(self, locator, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (expected_conditions.element_to_be_clickable(locator))
        return element

    def del_member(self, name):
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for value in elements:
            name_list.append(value.get_attribute('title'))
        n = name_list.index(name) + 2
        # print(name_list)
        # print(n)
        self.find(By.XPATH, f"(//input[@type='checkbox'])[{n}]").click()
        self.find(By.LINK_TEXT, "删除").click()
        self.find(By.LINK_TEXT, "确认").click()

    def get_datas1(self):
        with open(data_file, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
            return datas
# def test_get_cookie(self):
#     self.driver.get("https://work.weixin.qq.com/")
#     self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]')
#     time.sleep(20)
#     # opt = webdriver.ChromeOptions()
#     # opt.debugger_address = "127.0.0.1:9222"
#     # self.driver = webdriver.Chrome(options=opt)
#     # self.driver.get("https://work.weixin.qq.com/")
#     cookies = self.driver.get_cookies()
#     with open("data_cookie.yaml", "w", encoding="utf-8") as f:
#         yaml.dump(cookies, f)
