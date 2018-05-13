#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/05/05 09:51
# 创建Flask类应用对象,导入视图views

from flask import Flask

app = Flask(__name__, template_folder=r"..\templates")  # template_folder指定静态文件路径，默认为当前路径下的templates文件夹
# 先定义Flask对象后再导入views页面
from Study_flask.views import home
from Study_flask.views import select_data