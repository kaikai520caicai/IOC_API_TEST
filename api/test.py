# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 11:03
# @Auth: GLK
# @File: test.py
# @Software :PyCharm
import pandas as ps


def read_excel(path):
    sheet = ps.read_excel(path)
    data_list = sheet.values.tolist()
    return data_list


a = read_excel(r"D:\测试用例\data.xlsx")
print(a)
