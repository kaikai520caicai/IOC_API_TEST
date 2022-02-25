# _*_ coding: utf-8 _*_
# @Time : 2021/11/23 12:02
# @Auth: GLK
# @File: run.py
# @Software :PyCharm

import unittest
from BeautifulReport import BeautifulReport
import time
from util import send_email,BASE_DIR

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./testcase", pattern="test*.py", top_level_dir=None)
    filename = r"\report\{}测试报告".format(time.strftime("%Y%m%d%H%M%S"))
    BeautifulReport(suite).report(filename=filename,
                                  description="IOC接口测试", log_path=".")
    # 获取report的路径
    path = BASE_DIR+filename+".html"
    # 发送邮件
    send_email(path)


