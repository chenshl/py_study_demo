#!usr/bin/python
# coding=utf-8
# @author : csl
# @date   : 2018/03/09 23:20
'''利用随机数开发一个年会抽奖系统'''

import random
import copy
import time

names = ['王帝萍','郭春霞','陈海燕','赵霞','珠海','肖春燕','刘佳']
cnames = copy.deepcopy(names)
i = 0
while i < 2:
    random.shuffle(cnames)  #打乱名字顺序
    for n in range(0,5):
        print('抽奖中：%s' %cnames[n])
        time.sleep(0.5)
    i += 1
    print('中奖人员为：%s' %cnames.pop(n))
# print(cnames)
