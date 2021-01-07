# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from automation.web_automation.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        self.driver.switch_to.default_content()
        # self.driver.switch_to.parent_frame()
        print(self.driver.find_element(By.ID, 'submitBTN').text)