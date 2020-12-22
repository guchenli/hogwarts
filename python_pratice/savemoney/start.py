# -*- coding: utf-8 -*-
from send_money import send_money
from select_money import select_money

if __name__ == '__main__':

    while 1:
        a = input("查询当前存款，请输入工作时长（月）:")
        try:
            a = int(a)
            select_money(send_money(a))
            break
        except ValueError:
            print("请输入整数\n")
            continue
"""
"""