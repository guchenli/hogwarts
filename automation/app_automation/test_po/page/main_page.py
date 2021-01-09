# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from automation.app_automation.test_po.page.addresslist_page import AddressListPage
from automation.app_automation.test_po.page.base_page import BasePage


class MainPage(BasePage):

    def click_mail_list(self):
        self.find(By.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
