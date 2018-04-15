#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/11 23:00
# flask学习

from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def helloWorld():
    return "this is flask say 'hello world'!"

@app.route("/user/<username>", methods=["GET", "POST"])
def show_user_profile(username):
    return "this is flask say 'hello world' to %s" % username


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)