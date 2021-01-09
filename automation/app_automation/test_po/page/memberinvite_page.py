# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


from automation.app_automation.test_po.page.base_page import BasePage
from automation.app_automation.test_po.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):

    def addconnect_member(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return ContactEditPage(self.driver)

    def get_toast(self):
        toast_info = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_info

    def back(self):
        from automation.app_automation.test_po.page.addresslist_page import AddressListPage
        self.find(MobileBy.ID, "com.tencent.wework:id/gu_").click()
        return AddressListPage(self.driver)
