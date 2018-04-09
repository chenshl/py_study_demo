#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/03/28 21:38
# 调用接口
# 根据Excel表中的标识判断访问哪个接口

import Study_api_test.common.py_api_server as get_api
import Study_api_test.report.ready_datas as rd
import Study_api_test.report.result_process as rp

f_path = "../test_datas/api_test_case.xlsx"
sheet_name = "测试用例"

rd_test = rd.ready_datas_new(f_path, sheet_name).read_excel()
for data in rd_test:
    print(data["接口类型"])
    if data["接口类型"] == "douban":
        req = get_api.douban_api(data["域名"], data["请求类型"], data["请求参数"]).send()
        print(req)
        rp.result_datas(data["接口名称"], req[0], req[1]).write_result_2_Excel()
    elif data["接口类型"] == "baifubao":
        req = get_api.baifubao_api(data["域名"], data["请求类型"], data["请求参数"]).send()
        print(req)
        rp.result_datas(data["接口名称"], req[0], req[1]).write_result_2_Excel()