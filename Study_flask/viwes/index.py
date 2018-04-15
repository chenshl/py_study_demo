#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/15 15:56
# flask渲染jinja模板

from flask import Flask, render_template, request

app = Flask(__name__, template_folder=r"..\templates")  # template_folder指定静态文件路径，默认为当前路径下的templates文件夹

@app.route("/home/", methods=["GET", "POST"])
def index():
    return render_template("home.html")
    # return render_template('about.html',user='xiaotuo')  # 模板文件中的参数传递，一个参数
    # return render_template('about.html',**{'user':'xiaotuo})  # 用字典形式传递多个参数

@app.route("/FlaskTutorial", methods=["GET", "POST"])
def success():
    if request.method == "POST":
        email = request.form["email"]
        return render_template("success.html", email=email)
    else:
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002, debug=True)
