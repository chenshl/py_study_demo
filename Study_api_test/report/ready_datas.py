#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/03/28
# 从Excel表读取测试用例内容,然后返回一个列表/字典，根据列表第0个值为键，后面对应分别为值

import openpyxl
import xlrd

# 返回一个列表
class ready_datas(object):

    def __init__(self, excel_path, sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_name

    def read_07_excel(self):
        wb = openpyxl.load_workbook(self.excel_path)
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


# 返回一个字典（表格第一行为键）
class ready_datas_new(object):

    def __init__(self, excel_path, sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_neme
        # 打开文件
        self.data = xlrd.open_workbook(self.excel_path)
        # 锁定sheet表格
        self.table = self.data.sheet_by_name(self.sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def read_excel(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            reslut = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行去取对应的value值
                s["rowNum"] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                reslut.append(s)
                j += 1
            return reslut



if __name__ == "__main__":
    f_path = "../test_datas/api_test_case.xlsx"
    sheet_neme = "测试用例"
    # ready_datas(f_path, sheet_neme).read_07_excel()
    r = ready_datas_new(f_path, sheet_neme).read_excel()
    print("调用完成")
    print(r)
