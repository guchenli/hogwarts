# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestMouse:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    # 鼠标点击、双击、右键等操作
    def test_mouse_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        e_click = self.driver.find_element(By.XPATH, "/html/body/form/input[3]")
        e_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        e_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(e_click)
        action.double_click(e_doubleclick)
        action.context_click(e_rightclick)
        action.perform()

    # 移动鼠标到某个元素上
    def test_mouse_move(self):
        self.driver.get("https://v.qq.com/")
        e_move = self.driver.find_element(By.CSS_SELECTOR, ".svg_icon_time")
        action = ActionChains(self.driver)
        action.move_to_element(e_move).perform()

    # 拖拽某个元素到指定位置
    def test_mouse_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        e_drag = self.driver.find_element(By.ID, "dragger")
        e_drop = self.driver.find_element(By.XPATH, "/html/body/div[4]")
        action = ActionChains(self.driver)
        #action.drag_and_drop(e_drag, e_drop).perform()
        #先按住再释放
        action.click_and_hold(e_drag).release(e_drop).perform()

    def test_mouse_sendkey(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        e_send = self.driver.find_element(By.XPATH, "/html/body/label[1]/input")
        e_send.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(2)
        action.send_keys(Keys.SPACE)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE).perform()


