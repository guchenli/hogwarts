# -*- coding: utf-8 -*-
import time

from appium import webdriver
from automation.app_automation.test_po.page.base_page import BasePage
from automation.app_automation.test_po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:

            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(30)
        else:
            #根据caps内设置信息启动APP
            self.driver.launch_app()
        return self

    def stop(self):
        time.sleep(2)
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)

