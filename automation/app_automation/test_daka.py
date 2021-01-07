# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from automation.app_automation.base_work import BaseWork


class TestDemo0106(BaseWork):
    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        r = self.driver.find_element_by_id("com.tencent.wework:id/mn").text
        assert "外出打卡成功" == r