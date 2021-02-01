# -*- coding: utf-8 -*-
import pytest
import requests


class TestHomeWork:

    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww7f5427ae71cd08e9", "corpsecret": "yZ4SWfyNVlKVxpiScwUERHfbzBPUtLi6rgnQENkihqE"}
        r = requests.request(method="GET", url=url, params=params)
        self.token = r.json()["access_token"]
        assert r.json()["errcode"] == 0
        print(self.token)

    def test_create_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        data = {
            "tagname": "UIW",
            "tagid": 12}
        params = {
            "access_token": self.token
        }
        r = requests.request(method="POST", url=url, params=params, json=data)
        print(r.json())
        assert r.json()["errmsg"] == "created"

    def test_update_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        data = {
            "tagname": "UIW2",
            "tagid": 12}
        params = {
            "access_token": self.token
        }
        r = requests.request(method="POST", url=url, params=params, json=data)
        print(r.json())
        assert r.json()["errmsg"] == "updated"

    def test_delete_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token": self.token,
            "tagid": 12
        }
        r = requests.request(method="GET", url=url, params=params)
        print(r.json())
        assert r.json()["errmsg"] == "deleted"
