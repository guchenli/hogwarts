# -*- coding: utf-8 -*-
# 1/3要提前登录
import pytest


# 创建登录的fixture方法  autouse=True
# cope="class"  、function、class、module、session
@pytest.fixture(scope="class")
def login():
    username = "guchenli"
    password = 1234567
    print("登录操作")
    yield [username, password]
    print("退出登录")


def test_case1(login):
    # def test_case1():  fixture返回值
    print(f"login information: {login}")
    print("用例1")


def test_case2(ConnectDB):
    print("用例2")


def test_case3(login):
    # def test_case3():
    print("用例3")


@pytest.mark.usefixtures("login")
def test_case4():
    print("用例4")
