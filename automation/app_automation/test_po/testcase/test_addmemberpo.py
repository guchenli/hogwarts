# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pytest
import yaml

from automation.app_automation.test_po.page.app import App

def get_data():
    with open("../data/data.yaml") as f:
        data = yaml.safe_load(f)
        addnumber = data["add"]
        return addnumber

class TestAddMember:
    def setup(self):
        self.app =App()
        self.main = self.app.start()

    # @pytest.mark.parametrize("name,gender,phone,mailbox,identity",
    #                          [("张伟", "男", "17807131312", "291531981@qq.com", "普通成员")])
    @pytest.mark.parametrize("name,gender,phone,mailbox,identity",get_data())
    def test_add_member(self, name, gender, phone, mailbox, identity):
        add_member = self.main.goto_main().click_mail_list().click_add_member().addconnect_member().edit_name(name).\
            edit_gender(gender).edit_phone(phone).edit_email(mailbox).edit_identity(identity).click_save()
        toast_info = add_member.get_toast()
        assert toast_info == "添加成功"
        print("添加成员用例验证通过")
        #删除数据
        add_member.back().del_member(name)

    def teardown(self):
        self.app.stop()
