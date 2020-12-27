# -*- coding: utf-8 -*-
import pytest

from automation.web_automation.selenium_po.page.basepage import BasePage
from automation.web_automation.selenium_po.page.main_page import MainPage

a = BasePage().get_datas1()


class TestLogin:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,phone", [(a['data1']['name'], a['data1']['id'], a['data1']['phone'])])
    def test_po(self, name, id, phone):
        namelist = self.main.goto_contact_page().click_add_member(). \
            add_member(name, id, phone).get_member(name)
        assert name in namelist

    @pytest.mark.parametrize("name,id,phone", [(a['data2']['name'], a['data2']['id'], a['data2']['phone'])])
    def test_po1(self, name, id, phone):
        namelist = self.main.goto_contact_page1(). \
            add_member1(name, id, phone).get_member(name)
        assert name in namelist
