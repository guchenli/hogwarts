# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseWork:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = True
        # caps["platformVersion"] = 11
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["settings[waitForIdleTimeout]"] = 0  #动态页面时间设置0
        # caps["automationName"] = "uiautomator2"   工作引擎

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def find(self, MobileBy, locator):
        return self.driver.find_element(MobileBy, locator)

    def finds(self, MobileBy, locator):
        return self.driver.find_elements(MobileBy, locator)

    # 滑动到某个元素
    def moveto_text(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        'scrollIntoView(new UiSelector().'
                                        f'text("{text}").instance(0));')

    # 找兄弟元素,例：通过姓名匹配到必填的输入框,,用(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
    def BroSelect(self, text1, text2):
        # father_el = self.find(MobileBy.XPATH, f"//*[@text='{text1}']/..").get_attribute("resource-id")
        father_el = self.find(MobileBy.XPATH, f"//*[contains(@text,'{text1}')]/..").get_attribute("resource-id")
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                         f'new UiSelector().resourceId("{father_el}").\
                             childSelector(text("{text2}"))')

    # 显示等待某个元素可点击
    def wait_for_click(self, locator, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (expected_conditions.element_to_be_clickable(locator))
        return element

    # 添加成员
    def add_member(self, name, gender, phone, mailbox, identity):
        self.BroSelect("姓名　", "必填").send_keys(name)
        self.BroSelect("性别", "男").click()
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='男']")
        self.wait_for_click(locator)
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        self.BroSelect("手机　", "手机号").send_keys(phone)
        self.BroSelect("邮箱　", "选填").send_keys(mailbox)
        self.BroSelect("地址", "选填").click()
        while True:
            element = self.finds(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gz']")
            if len(element) > 0:
                break
        self.find(MobileBy.ID, "com.tencent.wework:id/dqz").click()
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gur']").click()
        self.BroSelect("身份", "普通成员").click()
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='普通成员']")
        self.wait_for_click(locator)
        self.find(MobileBy.XPATH, f"//*[@text='{identity}']").click()
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gur']").click()

    # 通讯录页面删除成员
    def del_member(self, name):
        self.moveto_text(f"{name}").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/guk").click()
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.moveto_text("删除成员").click()
        locator = (MobileBy.ID, "com.tencent.wework:id/b_4")
        self.wait_for_click(locator)
        self.find(MobileBy.ID, "com.tencent.wework:id/b_4").click()

    # 返回键
    def back(self):
        return self.find(MobileBy.ID, "com.tencent.wework:id/gu_").click()

    # 断言toast提示
    def assert_toast_text(self, text):
        toast_info = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert toast_info == text

