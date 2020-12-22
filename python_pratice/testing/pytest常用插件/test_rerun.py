# -*- coding: utf-8 -*-
from time import sleep

import pytest


def test_rerun():
    sleep(1)
    assert 1 == 1


def test_rerun1():
    sleep(1)
    assert 1 == 1


# 重跑次数 及 间隔时间
@pytest.mark.flaky(reruns=4, reruns_delay=2)
def test_rerun2():
    sleep(1)
    assert 2 == 3
