# -*- coding: utf-8 -*-
import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from automation.web_automation.base import Base


class TestLogin(Base):
    @pytest.mark.first
    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # time.sleep(20)
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, 'logout')))
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.get("https://work.weixin.qq.com/")
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("data_cookie.yaml", "w", encoding="utf-8") as f:
            yaml.dump(cookies, f)

    def test_login(self):
        # 先设置cookie前访问企业微信登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # cookies = [{'domain': '.qq.com', 'expiry': 1608134102, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608133911'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5131686'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854032715502'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '9927962889'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '7422715904'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325096208135'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854032715502'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '33890722491619668'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'nGMddW-CVmOXizgMciu0UrE2fvuXlxyQcm5B8-QwI8ranoFoxzldKJLMFQhEJ0o2'}, {'domain': '.qq.com', 'expiry': 1608220323, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1078009165.1608125222'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608156754, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2dfofjo'}, {'domain': '.qq.com', 'expiry': 1917602434, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'e02c445644c5000e'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639661218, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1671205923, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.468236373.1603616366'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610726045, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1636270647, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/', 'secure': False, 'value': '296671537233397100%2C3990517034126257000%2C3849677312729966000%2C85259127317738130'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s8707299479&pgvReferrer='}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False, 'value': '@QP2BaZCNF'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False, 'value': 'o0295532986'}, {'domain': '.qq.com', 'expiry': 1636270647, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/', 'secure': False, 'value': '1603616350%2C1604734647'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639669910, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608125221,1608133911'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'lj4A1GFeXb5TmNTJclM2hpZaDy4iGizc6_rotaH0Y2CEnr8eSPm3RKP9_tYfDWXB3BFNz2IgwUuFgR1lzMjfIeiNsj_hYR0SlUpkGOTHf8cI5hCgKt2Kh_jrH092fvDoS8vV7XDh_D8d6Cr9Up8jt2oIIe7Sgx3JQ24vSOu_IovhL4zXRU0C46vNFuttG33lgh-gp__oHQJvK4YnW0tdl0VY5S7koLCMzFcF087Knk7xArOw40JlwTW5JFT8392_QcKRZmbg_N7y3x-a7YDmwA'}, {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False, 'value': '0.8372867212793569'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '295532986'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'c47e416b277324ae62240ab64051e37fe4c09f2a8d06985362ab76018133c14f'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False, 'value': 's5222255616'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'eejcoVqmFZ'}]
        with open("./data_cookie.yaml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                # 把cookie传给driver
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, "menu_contacts").click()
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        # 死循环多次点击直到新页面的元素出现
        while True:
            self.driver.find_element(*ele).click()
            element = self.driver.find_elements(By.ID, 'username')
            if len(element) > 0:
                break
        self.driver.find_element(By.ID, "username").send_keys("gu")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("chenlii")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("guchenli01")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("17807231351")
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("12")
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'保存')])[4]").click()

        text_info = self.driver.find_element(By.ID, "js_tips").text
        assert text_info == "保存成功"
        # try:
        #     assert text_info == "保存成功1"
        #     print("验证通过")
        # except Exception as e:
        #     print(f"验证失败:{e}")fin
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # 设一个空列表，将页面名称都添加进这个列表中再断言
        name_list = []
        for value in elements:
            name_list.append(value.get_attribute('title'))
        assert 'gu' in name_list
        time.sleep(10)
        self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确认").click()
        text_info1 = self.driver.find_element(By.ID, "js_tips").text
        assert text_info1 == "正在删除..."
        # try:
        #     assert text_info1 == "删除成功"
        #     print("验证通过")
        # except Exception as e:
        #     print(f"验证失败:{e}")
