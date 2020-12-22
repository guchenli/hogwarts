# -*- coding: utf-8 -*-
from function_gcl import *

if __name__ == '__main__':
    A = get_datas()
    name = A["default"]["name"]
    color = A["default"]["color"]
    age = A["default"]["age"]
    sex = A["default"]["sex"]
    hair = A["default"]["hair"]
    c = Cat(name, color, age, sex, hair)
    print(f"猫的名字是：{c.name}\n猫的颜色是：{c.color}\n猫的年龄是：{c.age}\n猫的性别是："
          f"{c.sex}\n猫的毛发是：{c.hair}")
    c.skill()
    print()

    name = A["default1"]["name"]
    color = A["default1"]["color"]
    age = A["default1"]["age"]
    sex = A["default1"]["sex"]
    hair = A["default1"]["hair"]
    d = Dog(name, color, age, sex, hair)
    print(f"狗的名字是：{d.name}\n狗的颜色是：{d.color}\n狗的年龄是：{d.age}\n狗的性别是："
          f"{d.sex}\n狗的毛发是：{d.hair}")
    d.skill()
