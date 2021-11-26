# _*_ coding: utf-8 _*_
# @Time : 2021/11/26 14:17
# @Auth: GLK
# @File: Comprehensive_security_api.py
# @Software :PyCharm
from base.base import Run_Main

class Comprehensive_Security_Api():
    def __init__(self):
        self.run = Run_Main()

    def comprehensive_security_api(self,url,json,headers,method):
        return self.run.run(url=url,json=json,headers=headers,method=method)