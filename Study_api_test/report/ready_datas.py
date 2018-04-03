#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/03/28
# 从Excel表读取测试用例内容,然后返回一个列表，根据列表第0个值为键，后面对应分别为值

import openpyxl

class ready_datas(object):

    def __init__(self, f_path, sheet_name):
        self.f_path = f_path
        self.sheet_name = sheet_name

    def read_07_excel(self):
        wb = openpyxl.load_workbook(self.f_path)
        sheet = wb[self.sheet_name]
        result = []
        for row in sheet.rows:
            rresult = []
            for cell in row:
                # print(cell.value)
                rresult.append(cell.value)
            result.append(rresult)
        # print(result)
        return result

if __name__ == "__main__":
    f_path = "../test_datas/api_test_case.xlsx"
    sheet_neme = "测试用例"
    ready_datas(f_path, sheet_neme).read_07_excel()
    print("调用完成")
