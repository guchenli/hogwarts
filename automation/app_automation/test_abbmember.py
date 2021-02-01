# -*- coding: utf-8 -*-

import pytest
from appium.webdriver.common.mobileby import MobileBy

from automation.app_automation.base_work import BaseWork


class TestAddMember(BaseWork):
    @pytest.mark.parametrize("name,gender,phone,mailbox,identity",[("张伟","男","17807231352","295532981@qq.com","普通成员")])
    def test_add_member(self, name, gender, phone, mailbox, identity):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.moveto_text("添加成员").click()
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.add_member(name, gender, phone, mailbox, identity)
        self.assert_toast_text("添加成功")
        self.back()
        self.del_member(name)