# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[123, "bbbb", "ccccc"])
def login1(request):
    # print(request.param)
    data = request.param
    print("获取测试数据")
    return  data

def test_case1(login1):

    print(f"用例  {login1}")