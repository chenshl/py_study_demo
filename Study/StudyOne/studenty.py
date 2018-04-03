#!usr/bin/env python3
# -*- coding:utf-8 -*-

"""使用@property
   python的内置@property装饰器就是负责把一个方法变成属性调用的;
   把一个getter方法变成属性只需要加上@property就可以了；
   此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
   还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
"""
__author__ = "csl"

class Studenty(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must be 0 ~ 100")
        self._score = value

    @property
    def score1(self):
        return self._score * 100


s = Studenty()
s.score = 10
print("分数为：%s   换成100分为：%s" % (s.score, s.score1))
