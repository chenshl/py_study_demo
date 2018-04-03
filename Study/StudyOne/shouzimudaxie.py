# -*- coding:utf-8 -*-

# map(x, y)函数的使用:x为要调用的函数本身(只需要传入方法名即可)，y为执行迭代的序列
from functools import reduce


def normalize(name):
    return name.capitalize()

def normalize2(name):
    return name[:1].upper() + name[1:].lower()  # 字符串拼拼接的方法

def prod(list):
    def chengfa(x, y):
        return x * y
    return reduce(chengfa, list)

L1 = ["KHJKJ", "hjhUJHJH", "jjUUJHBHG"]
L2 = list(map(normalize, L1))
print(L2)

L3 = list(map(normalize2, L1))
print(L3)

print(prod([1, 2, 3, 4, 5, 6]))
