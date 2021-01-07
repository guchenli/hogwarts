# -*- coding: utf-8 -*-
import time

from appium import webdriver


class Base:
    def setup(self):
        desire_cap = {
            "platformName": "android",  #安卓
            "deviceName": "emulator-5554",  #设备
            "appPackage": "com.xueqiu.android",  #包名
            "appActivity": ".common.MainActivity",  #activity名
            "noReset": True,  #当前session下不会重置会话默认false
            "platformVersion": "11", #版本
            "unicodeKeyboard": True,  # 这两个设置 send_keys()传入中文时需要配置,设置之后会有Appium的输入法守护来执行输入操作
            "resetKeyboard": True,
            # "dontStopAppOnReset": True  #不终止当前APP上的内容,调试时使用
            "settings[waitForIdleTimeout]": 0
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
