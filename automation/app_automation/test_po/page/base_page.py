# -*- coding: utf-8 -*-

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, MobileBy, locator):
        return self.driver.find_element(MobileBy, locator)

    def finds(self, MobileBy, locator):
        return self.driver.find_elements(MobileBy, locator)

    # 滑动到某个元素
    def moveto_text(self, text):
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
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

    # 断言toast提示
    def assert_toast_text(self, text):
        toast_info = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert toast_info == text
