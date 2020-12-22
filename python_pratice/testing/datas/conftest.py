# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="module")
def ConnectDB():
    print("链接数据库")
    yield
    print("断开数据库")