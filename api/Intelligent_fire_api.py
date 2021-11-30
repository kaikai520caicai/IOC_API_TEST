# _*_ coding: utf-8 _*_
# @Time : 2021/11/30 11:10
# @Auth: GLK
# @File: Intelligent_fire_api.py
# @Software :PyCharm
from base.base import Run_Main


class Intelligent_Fire_Api():
    """
    智慧消防接口
    """
    def __init__(self):
        self.run = Run_Main()

    def intelligent_fire_api(self, url,params, headers, method):
        return self.run.run(url=url,params=params, headers=headers, method=method)
