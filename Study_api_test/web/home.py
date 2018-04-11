#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/11 23:00
# flask学习

from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "this is flask say 'hello world'!"

@app.route("/user/<username>")
def show_user_profile(username):
    return "this is flask say 'hello world' to %s" % username


if __name__ == "__main__":
    app.run(debug=True)