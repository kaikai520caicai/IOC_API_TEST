# _*_ coding: utf-8 _*_
# @Time : 2021/11/26 13:47
# @Auth: GLK
# @File: carTraffic_api.py
# @Software :PyCharm
from base.base import Run_Main


class CarTraffic_Api():
    """
    近一周通行趋势
    """

    def __init__(self):
        self.run = Run_Main()

    def carTraffic_api(self, url, method):
        return self.run.run(url=url, method=method)
