# -*- coding: utf-8 -*-
import allure
import pytest

from python_pratice.Python_code.calc import Calculator

@allure.feature("测试计算器")
class TestCalc:
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算完成")
    # @pytest.mark.parametrize(
    #     "a,b,expect",
    #     add_datas, ids=add_myid
    # )
    @pytest.mark.add
    @pytest.mark.first
    @allure.story("测试加法")
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            # with allure.step("计算两数相加和"):
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 浮点数判断
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        print(f"{get_add_datas[0]}+{get_add_datas[1]}={get_add_datas[2]}")
        assert result == get_add_datas[2]

    @pytest.mark.div
    @pytest.mark.run(order=3)
    @allure.story("测试除法")
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        print(f"{get_div_datas[0]}/{get_div_datas[1]}={get_div_datas[2]}")
        assert result == get_div_datas[2]

    @pytest.mark.mul
    @pytest.mark.run(order=2)
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_mul_datas):
        result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        print(f"{get_mul_datas[0]}*{get_mul_datas[1]}={get_mul_datas[2]}")

        assert result == get_mul_datas[2]

    @pytest.mark.sub
    @pytest.mark.run(order=1)
    @allure.story("测试减法")
    def test_sub(self, get_calc, get_sub_datas):
        result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        print(f"{get_sub_datas[0]}*{get_sub_datas[1]}={get_sub_datas[2]}")
        assert result == get_sub_datas[2]
    # @pytest.mark.parametrize(
    #     "a,b,expect",
    #     div_datas, ids=div_myid
    # )
    # def test_div(self, get_calc, a, b, expect):
    #     result = None
    #     # 异常处理
    #     try:
    #         result = get_calc.div(a, b)
    #         if isinstance(result, float):
    #             result = round(result, 2)
    #     except Exception as e:
    #         print(e)
    #     print(f"{a}/{b}={result}")

    # def test_add1(self):
    #     # 实例化计算器的类b
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.2)
    #     assert round(result, 2) == 0.3
    #
    # def test_add2(self):
    #     # 实例化计算器的类
    #     # calc = Calculator()
    #     result = self.calc.add(-1, 2)
    #     assert result == 1
