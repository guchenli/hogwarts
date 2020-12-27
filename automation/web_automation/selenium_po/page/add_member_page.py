# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from automation.web_automation.selenium_po.page.basepage import BasePage
from automation.web_automation.selenium_po.page.contact_page import ContactPage

#添加成员页面
class AddMemberPage(BasePage):
    _ele_name = (By.ID,"username")
    _ele_id = (By.ID, "memberAdd_acctid")
    _ele_phone = (By.ID, "memberAdd_phone")
    def add_member(self, name, id, phone):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_phone).send_keys(phone)
        self.find(By.XPATH, "(//a[contains(text(),'保存')])[4]").click()
        #返回给通讯录页面
        return ContactPage(self.driver)

    def add_member1(self, name, id, phone):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_phone).send_keys(phone)
        self.find(By.XPATH, "(//a[contains(text(),'保存')])[4]").click()

        return ContactPage(self.driver)
