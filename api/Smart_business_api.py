# _*_ coding: utf-8 _*_
# @Time : 2021/11/30 13:56
# @Auth: GLK
# @File: Smart_business_api.py
# @Software :PyCharm
from base.base import Run_Main


class Smart_Business_Api():
    """
    智慧商圈接口
    """
    def __init__(self):
        self.run = Run_Main()

    def smart_business_api(self, url, params, headers, method):
        return self.run.run(url=url, params=params, headers=headers, method=method)
