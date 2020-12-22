# -*- coding: utf-8 -*-
from typing import List

import pytest
import yaml, os
#
from python_pratice.Python_code.calc import Calculator

#  错误导入：from Python_code.calc import Calculator
yaml_file_path = os.path.dirname(__file__) + "\datas\calc.yaml"
# print(yaml_file_path)

with open(yaml_file_path) as f:
    data_add = yaml.safe_load(f)
    # for i in data_add.keys():
    #     data = data_add[i]
    #     datas = data["datas"]
    #     myid = data["myid"]
    add_datas = data_add["add"]["datas"]
    add_myid = data_add["add"]["myid"]
    div_datas = data_add["div"]["datas"]
    div_myid = data_add["div"]["myid"]
    sub_datas = data_add["sub"]["datas"]
    sub_myid = data_add["sub"]["myid"]
    mul_datas = data_add["mul"]["datas"]
    mul_myid = data_add["mul"]["myid"]


@pytest.fixture(params=add_datas, ids=add_myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    # print(f"request.param的数据是：{data}")
    yield data
    print("计算完成")


@pytest.fixture(params=div_datas, ids=div_myid)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算完成")


@pytest.fixture(params=sub_datas, ids=sub_myid)
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算完成")


@pytest.fixture(params=mul_datas, ids=mul_myid)
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算完成")


@pytest.fixture(scope="module")
def ConnectDB():
    print("链接数据库")
    yield
    print("断开数据库")


@pytest.fixture(scope="class")
def get_calc():
    # print("获取计算器实例")
    calc = Calculator()
    return calc


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # 实现用例反转执行
    items.reverse()
    # 解决编码问题
    for item in items:
        item.name = item.name.encode("UTF-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("UTF-8").decode("unicode-escape")
