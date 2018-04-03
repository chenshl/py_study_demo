#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/03/28 21:38
# 调用接口

import Study_api_test.common.py_api_server as get_api
import Study_api_test.report.ready_datas as rd

f_path = "../test_datas/api_test_case.xlsx"
sheet_neme = "测试用例"
rd_test = rd.ready_datas(f_path, sheet_neme).read_07_excel()
# print(rd_test)

for i in range(1, len(rd_test)):
    if rd_test[i][1] == "post":
        t2 = get_api.testapi(rd_test[i][0], rd_test[i][1]).send()
    else:
        t2 = get_api.testapi_next(rd_test[i][0], rd_test[i][1]).send()
    print("调用接口：%s  访问方式：%s   调用参数：%s" %(rd_test[i][0], rd_test[i][1], rd_test[i][2]))
    print(t2)
    print(t2["code"])
print("接口执行完毕")