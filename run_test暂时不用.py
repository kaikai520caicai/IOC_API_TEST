# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 13:34
# @Auth: GLK
# @File: run_test暂时不用.py
# @Software :PyCharm
import unittest, time
from HTMLTestRunner import HTMLTestRunner
from util import BASE_DIR
path = BASE_DIR+"/testcase/"


def createsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(path, pattern='test_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
        print(testunit)
    return testunit


now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
filename = BASE_DIR +"/report/"+ now + "_result.html"

fp = open(filename, 'wb')

runner = HTMLTestRunner(stream=fp, title=u'ioc接口测试报告', description=u'用例执行情况：')

runner.run(createsuite())

# 关闭文件流，不关的话生成的报告是空的
fp.close()
