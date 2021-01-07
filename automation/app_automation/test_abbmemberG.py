# -*- coding: utf-8 -*-
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from automation.app_automation.base_work import BaseWork


class TestAddMember(BaseWork):
    def test_add_member(self):
        # self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.moveto_text("添加成员")
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.find(By.XPATH, "//*[@text='手动输入添加']").click()
        self.add_member("张伟","男","17807231351","295532981@qq.com","普通成员")
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiSelector().resourceId("com.tencent.wework:id/b2k").\
        #                          childSelector(text("必填"))').send_keys("张伟")
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiSelector().resourceId("com.tencent.wework:id/cm2").\
        #                          childSelector(text("男"))').click()
        # self.BroSelect("com.tencent.wework:id/b2k", "必填").send_keys("张伟")
        # self.BroSelect("com.tencent.wework:id/cm2", "男").click()
        # locator = (By.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='男']")
        # self.wait_for_click(locator)
        # self.find(By.XPATH,"//*[@text='男']").click()
        # self.BroSelect("com.tencent.wework:id/e7c", "手机号").send_keys("17807231350")
        # self.BroSelect("com.tencent.wework:id/b2k", "选填").send_keys("295532981@qq.com")
        # self.BroSelect("com.tencent.wework:id/gy", "选填").click()
        # while True:
        #     element = self.finds(By.XPATH, "//*[@resource-id='com.tencent.wework:id/gz']")
        #     if len(element) > 0:
        #         break
        # # self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/gz']").send_keys("123")
        # # self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/h1a' and @text='123教育']").click()
        # self.find(By.ID, "com.tencent.wework:id/dqz").click()
        # self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/gur']").click()
        # self.BroSelect("com.tencent.wework:id/bgi", "普通成员").click()
        # locator = (By.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='普通成员']")
        # self.wait_for_click(locator)
        # self.find(By.XPATH, "//*[@text='普通成员']").click()
        # self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/gur']").click()
        # print(self.driver.page_source) 打印页面内容
        toastinfo = self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
        # print(toastinfo)
        assert toastinfo == "添加成功"
        self.find(By.ID, "com.tencent.wework:id/gu_").click()
        self.del_member("张伟")