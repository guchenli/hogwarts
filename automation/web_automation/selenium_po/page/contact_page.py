# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from automation.web_automation.selenium_po.page.basepage import BasePage

#通讯录页面
class ContactPage(BasePage):
    def click_add_member(self):
        from automation.web_automation.selenium_po.page.add_member_page import AddMemberPage
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # 显示等待元素可点击
        self.wait_for_click(ele)
        # 死循环多次点击直到新页面的元素出现
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            element = self.finds(By.ID, 'username')
            if len(element) > 0:
                break
        #返回给添加成员页面
        return AddMemberPage(self.driver)

    def get_member(self, name):
        text_info = self.find(By.ID, "js_tips").text
        assert text_info == "保存成功"
        # try:
        #     assert text_info == "保存成功1"
        #     print("验证通过")
        # except Exception as e:
        #     print(f"验证失败:{e}")fin
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # 设一个空列表，将页面名称都添加进这个列表中再断言
        name_list = []
        for value in elements:
            name_list.append(value.get_attribute('title'))
        self.del_member(name)
        return name_list