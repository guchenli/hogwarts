# -*- coding: utf-8 -*-
##  pytest -n 3 3个线程跑
#--html=report.html --self-contained-html
from time import sleep


def test_foo():
    sleep(2)
    assert True

def test_bar():
    sleep(2)
    assert True

def test_ba():
    sleep(2)
    assert True
