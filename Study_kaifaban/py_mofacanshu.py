#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/22 22:24
# 魔法参数*args和**kwargs的用法
# *args可以捕获到所有的位置参数（非keyword参数）；**kwargs可以捕获到所有的keywords参数

def args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *args:", arg)

alist = [1, 'python1', 'helloworld1', 'test1']
atuple = (2, 'python2', 'helloworld2', 'test2')
args(*alist)
args(alist)
args(*atuple)
args(atuple)

def kwargs(f_arg, **kwargs):
    print("NO:", f_arg)
    for k, w in kwargs.items():
        print("%s == %s" % (k, w))

adict = {"name":"Jack", "sex":"Men", "age":"22"}
kwargs(3, **adict)
