# -*- coding: utf-8 -*-
import pytest


def test_a():
    print("一一一一")

def test_b():
    print("二二二二")

def test_c():
    assert 1 == 1

@pytest.mark.parametrize("a",[1,2,3])
@pytest.mark.parametrize("b",[4,5,6])
def test_param(a,b):
    print(f"a = {b},b = {b}")