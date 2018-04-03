#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""如果一个类想被用于for...in...循环，就必须实现一个__iter__()方法，
   该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
   拿到循环的下一个值，遇到StopIteration错误时退出循环
"""
__author__ = "chensl"

class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        # self.a = self.b
        # self.b = self.a + self.b  # 计算下一个值
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

if __name__ == "__main__":
    for n in Fib():
        print(n)
