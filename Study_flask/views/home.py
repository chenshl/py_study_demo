#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/05/04 00:37
# 主页

from flask import Flask, render_template, request
from Study_flask.base.flask_object import app

@app.route("/home/", methods=["GET", "POST"])
def index():
    return render_template("home.html")


