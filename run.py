# _*_ coding: utf-8 _*_
# @Time : 2021/11/23 12:02
# @Auth: GLK
# @File: run.py
# @Software :PyCharm

import unittest
from BeautifulReport import BeautifulReport
import time

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./testcase", pattern="test*.py", top_level_dir=None)
    BeautifulReport(suite).report(filename="./report/{}测试报告".format(time.strftime("%Y%m%d%H%M%S")),
                                  description="IOC接口测试", log_path=".")

