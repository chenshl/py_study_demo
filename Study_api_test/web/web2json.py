#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/14 20:39
# 访问web页面返回json格式字符(自定义响应)

from flask import Flask, jsonify
from werkzeug.wrappers import Response
from Study_api_test.common.py_api_server import douban_api
import json

app = Flask(__name__)  # 实例化app对象

class JSONResponse(Response):

    default_mimetype = "application/json"

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):  # 如果response是一个字典类型
            response = jsonify(response)  # 转换为json格式
        return super(JSONResponse, cls).force_type(response, environ)

app.response_class = JSONResponse

@app.route("/about/", methods=["GET", "POST"])
def about():
    # ensure_ascii=False).encode('gb2312')处理json中的中文乱码
    # return json.dumps({"type":"我是字典", "功能":"可以转换为json"}, ensure_ascii=False).encode('gb2312')
    # 调用接口返回接口数据
    book_name = 'q="百年孤独"'
    result = douban_api("https://api.douban.com/v2/book/search", "get", book_name).send()
    return json.dumps(result, ensure_ascii=False).encode('utf-8')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)