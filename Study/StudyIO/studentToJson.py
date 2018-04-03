#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
python的dict对象可以直接转换为json的{}，不过很多时候我们更喜欢用class表示对象，然后转换成json
author:chensl
"""

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

s = Student("Bob", 20, 88)
print(json.dumps(s, default=Student.student2dict))
