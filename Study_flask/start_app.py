#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/05/03 22:53
# 封装flask启动代码

# from flask import Flask
from Study_flask.base.flask_object import app

app.run(host="0.0.0.0", port=9001, debug=True)

