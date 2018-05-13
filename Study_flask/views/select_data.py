#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/05/13 16:41
# 查询数据库页面

from flask import Flask, render_template, request
from Study_flask.base.flask_object import app
from Study_flask.common import db_operating as db

@app.route("/select/", methods=["GET", "POST"])
def select1():
    return render_template("select.html")


@app.route("/sql", methods=["GET", "POST"])
def select_result():
    if request.method == "POST":
        sql = request.form["sql"]
        sql_result = db.db_select(sql)
        return render_template("success.html", sql_result=sql_result)
    else:
        return render_template("404.html")