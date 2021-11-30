# _*_ coding: utf-8 _*_
# @Time : 2021/11/30 14:50
# @Auth: GLK
# @File: Intelligent_life_api.py
# @Software :PyCharm
from base.base import Run_Main


class Intelligent_Life_Api():
    """
    智慧生活和能效管理接口
    """
    def __init__(self):
        self.run = Run_Main()

    def intelligent_life_api(self, url, headers, method):
        return self.run.run(url=url, headers=headers, method=method)
