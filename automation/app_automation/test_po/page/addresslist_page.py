# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from automation.app_automation.test_po.page.base_page import BasePage
from automation.app_automation.test_po.page.memberinvite_page import MemberInvitePage


class AddressListPage(BasePage):

    def click_add_member(self):
        self.moveto_text("添加成员").click()
        return MemberInvitePage(self.driver)

    # 通讯录页面删除成员
    def del_member(self, name):
        self.moveto_text(f"{name}").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/guk").click()
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.moveto_text("删除成员").click()
        locator = (MobileBy.ID, "com.tencent.wework:id/b_4")
        self.wait_for_click(locator)
        self.find(MobileBy.ID, "com.tencent.wework:id/b_4").click()