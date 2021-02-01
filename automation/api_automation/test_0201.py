# -*- coding: utf-8 -*-
import requests


# def test_demo():
#     r = requests.request(method="GET", url="https://httpbin.testing-studio.com/get")
#     print(r.json())
#     print(r.status_code)
#     print(r.text)

class TestWeixin:

    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww7f5427ae71cd08e9", "corpsecret": "yZ4SWfyNVlKVxpiScwUERHfbzBPUtLi6rgnQENkihqE"}
        r = requests.request(method="GET", url=url, params=params)
        self.token = r.json()["access_token"]
        assert r.json()["errcode"] == 0
        print(self.token)

    def test_create_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            "name": "广州研发中心1",
            "name_en": "GZYF1",
            "parentid": 1,
            "order": 1,
            "id": 3}
        params = {
            "access_token": self.token
        }

        r = requests.request(method="POST", url=url, params=params, json=data)
        assert r.json()["errcode"] == 0

    def test_update_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/" \
              f"department/update?access_token={self.token}"
        data = {
            "name": "广州研发中心12",
            "name_en": "RDGZ2",
            "parentid": 1,
            "order": 1,
            "id": 3
        }
        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errmsg"] == "updated"

    def test_delete_department(self):
        id = 3
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}"
        r = requests.request(method="GET", url=url)
        assert r.json()["errmsg"] == "deleted"

    def test_get_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        print(r.json())