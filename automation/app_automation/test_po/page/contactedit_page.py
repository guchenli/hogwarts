# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from automation.app_automation.test_po.page.base_page import BasePage


class ContactEditPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def edit_name(self,name):
        self.BroSelect("姓名　", "必填").send_keys(name)
        return self

    def edit_gender(self,gender):
        self.BroSelect("性别", "男").click()
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='男']")
        self.wait_for_click(locator)
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        return self

    def edit_phone(self,phone):
        self.BroSelect("手机　", "手机号").send_keys(phone)
        return self

    def edit_email(self,mailbox):
        self.BroSelect("邮箱　", "选填").send_keys(mailbox)
        return self

    def edit_identity(self,identity):
        self.BroSelect("身份", "普通成员").click()
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='普通成员']")
        self.wait_for_click(locator)
        self.find(MobileBy.XPATH, f"//*[@text='{identity}']").click()
        return self

    def click_save(self):
        from automation.app_automation.test_po.page.memberinvite_page import MemberInvitePage
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gur']").click()
        return MemberInvitePage(self.driver)
