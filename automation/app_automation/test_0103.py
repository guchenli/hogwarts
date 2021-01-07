# -*- coding: utf-8 -*-
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from automation.app_automation.base_xueqiu import Base


class TestWD(Base):
    # def setup(self):
    #     desire_cap = {
    #         "platformName": "android",
    #         "deviceName": "emulator-5554",
    #         "appPackage": "com.xueqiu.android",
    #         "appActivity": ".common.MainActivity",
    #         "noReset": True
    #     }
    #     self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
    #     self.driver.implicitly_wait(10)
    # def teardown(self):
    #     self.driver.quit()
    def test1(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        #and 多重判断定位
        el3 = self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el3.click()
        ali_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert ali_price > 200
        # self.driver.find_element_by_accessibility_id()

    def test_attr(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        #is_enabled是否可用
        ele_enabled = el1.is_enabled()
        print(ele_enabled, el1.text, el1.size, el1.location)
        #当搜素可用时，点击搜索
        if ele_enabled == True:
            el1.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            el2 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            #判断输入阿里巴巴时联想词是否可点击，可点击时再点击，也可以获取元素属性判断
            # ele_displayed = el2.get_attribute("displayed")
            ele_displayed = el2.is_displayed()
            # if ele_displayed == "true":
            if ele_displayed == True:
                self.driver.find_element_by_xpath(
                    "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        #先生成已给action
        action = TouchAction(self.driver)
        #获取当前屏幕分辨率大小
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        print(window_rect, width, height)
        x1 = width*0.5
        y_start = height*0.8
        y_end = height*0.2
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_touchaction_unlock(self):
        print('解锁手势密码')
        action = TouchAction(self.driver)
        action.press().move_to().move_to().release().perform()

    def test_xpath(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # and 多重判断定位
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # time.sleep(2)
        #xpath先获取到股票的代码，通过找到相同的父（爷爷节点）节点，再父节点下找到对于的元素
        price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(price)

    def test_uiaut(self):
        # self.driver.find_element_by_xpath("//*[@text='我的']").click()
        #里面要用双引号,组合定位resourceId().text()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId\
                ("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId\
                ("com.xueqiu.android:id/login_password")').send_keys("12345678")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId\
                ("com.xueqiu.android:id/button_next")').click()
        #父子关系定位,父节点下text属性的元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId().childSelector(text())')
        #兄弟节点
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId().fromParent(text())')
    def test_uiaut1(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        #滚动查找元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).\
                                                        scrollIntoView(new UiSelector().text("京东(JD)").instance(0))').click()

    def test_wait(self):
        pass
