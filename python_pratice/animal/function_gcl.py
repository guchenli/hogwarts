# -*- coding: utf-8 -*-
import yaml

data_file = "animaldata.yaml"


class Animal:
    name: str = None
    color: str = "white"
    age: int = 0
    sex: str = "male"

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def run(self):
        print(f"{self.name}can running")

    def shout(self):
        print(f"{self.name} can shouting")


class Cat(Animal):
    hair = ""
    skill = ""

    def __init__(self, name, color, age, sex, hair):
        self.hair = hair
        super().__init__(name, color, age, sex)

    def skill(self):
        print(f"{self.name} can Catching mice")

    def shout(self):
        print(f"{self.name} can mew")


class Dog(Animal):
    hair = ""

    def __init__(self, name, color, age, sex, hair):
        self.hair = hair
        super().__init__(name, color, age, sex)

    def skill(self):
        print(f"{self.name} can Touch home")

    def shout(self):
        print(f"{self.name} can bowwow")


def get_datas():
    with open(data_file, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        return datas
