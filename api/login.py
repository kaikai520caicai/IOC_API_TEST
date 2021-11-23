# _*_ coding: utf-8 _*_
# @Time : 2021/11/22 10:22
# @Auth: GLK
# @File: login.py
# @Software :PyCharm
from base.base import Run_Main


class Login_Api():
    def __init__(self):
        self.run = Run_Main()

    def login_api(self, url, data, headers, method):
        return self.run.run(url=url, data=data, headers=headers, method=method)
