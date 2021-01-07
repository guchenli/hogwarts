# -*- coding: utf-8 -*-
from selenium import webdriver


def test_get_cookie():
  # 调用chromeoptions方法
  opt = webdriver.ChromeOptions()
  # 设置复用浏览器的地址
  opt.debugger_address = "127.0.0.1:9222"
  driver = webdriver.Chrome(options=opt)
  # 设置隐式等待
  driver.implicitly_wait(10)
  cookies = driver.get_cookies()
  print(cookies)