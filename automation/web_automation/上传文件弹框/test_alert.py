# -*- coding: utf-8 -*-
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from automation.web_automation.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #进入frame
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element(By.ID, 'draggable')
        drop = self.driver.find_element(By.ID, 'droppable')
        #定义动作 perform执行动作
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(3)
        #进入弹框alert 点击确认
        self.driver.switch_to_alert().accept()
        #切回默认的frame
        self.driver.switch_to_default_content()
        self.driver.find_element(By.ID, 'submitBTN').click()
