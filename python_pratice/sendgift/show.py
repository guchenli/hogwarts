# -*- coding: utf-8 -*-
# from gift import have_gift
import gift


# 展示礼物
def show():
    if gift.have_gift == True:
        print("收到礼物了")
    else:
        print("没有礼物")
