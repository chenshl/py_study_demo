#! /user/bin/python
# -*- coding: UTF-8 -*-
# @author : csl
# @date   : 2018/01/21 10:06
'''turtle库练习绘制一个蟒蛇图型'''
import turtle
import time

# tt = turtle.Turtle()
# tt.color("red", "yellow")
# tt.begin_fill()
# for _ in range(50):
#     tt.forward(200)
#     tt.left(170)
#     tt.end_fill()

# tt = turtle.Turtle()
# def drawSnake(rad, angle, len, neckrad):
#     for i in range(len):
#         tt.circle(rad, angle)
#         tt.circle(-rad, angle)
#     tt.circle(rad, angle/2)
#     tt.fd(rad)
#     tt.circle(neckrad+1, 180)
#     tt.fd(rad*2/3)
#
# def start():
#     tt.setundobuffer(100)
#     pythonsize = 30
#     tt.pensize(pythonsize)
#     tt.pencolor("blue")
#     tt.seth(-40)
#     drawSnake(40, 80, 5, pythonsize/2)
#
# start()

def reverse(s):
    if s == "":
        return s
    else:
        s1 = s[0]
        s2 = s[1:]
        return reverse(s[1:]) + s[0]
s3 = reverse('hello')