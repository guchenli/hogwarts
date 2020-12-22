# -*- coding: utf-8 -*-
import yaml

with open("./datas/calc.yaml") as f:
    data_add = yaml.safe_load(f)
    a = data_add.keys()
    # b = range(len(a))
    # print(b)
    for i in data_add.keys() :
        c = data_add[i]
        d = c["datas"]
        e = c["myid"]
        print(d,"\n",e)
    # add_key = data_add.keys()
    # list = list(add_key)
    # add_datas = data_add["add"]["datas"]
    # add_myid = data_add["add"]["myid"]
    # div_datas = data_add["div"]["datas"]
    # div_myid = data_add["div"]["myid"]
    # print(data_add)
    # print(add_datas,add_myid,div_datas,div_myid)
    # print("\n",list)
    # print(type(add_key))
# a = 0.3
# b = round(a)
# c = round(a, 2)
# print(b, c)
