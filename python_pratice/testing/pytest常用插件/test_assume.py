# -*- coding: utf-8 -*-
#执行所有断言
import pytest
def test_as():
    # assert 1 == 2
    # assert False == True
    # assert 100 == 102
    # assert  2 == 2

    pytest.assume(1 == 2)
    pytest.assume(1 == 3)
    pytest.assume(1 == 1)