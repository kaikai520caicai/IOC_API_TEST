# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 14:40
# @Auth: GLK
# @File: test_query_api.py
# @Software :PyCharm
import requests
import unittest
from api.api_query import Api_Query
from base.base import Run_Main
import warnings
from config.config import Logger
from util import get_token

mylogger = Logger(logger="test_query_api").getlog()


class Test_Query_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mylogger.info("开始测试查询接口")

    @classmethod
    def tearDownClass(cls):
        mylogger.info("结束测试查询接口")

    def setUp(self):
        mylogger.info("-------开始执行测试用例-------")
        warnings.simplefilter('ignore', ResourceWarning)  # 消除报警的
        self.api_query = Api_Query()
        self.run = Run_Main()

    def tearDown(self):
        mylogger.info("-----结束一条测试用例------")
        self.run.close_session()

    def test_query_api_success(self):
        url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/blacklist/queryBlacklist"
        json = {
            "startTime": "2021-09-01",
            "endTime": "2021-11-16",
            "projectIds": "t1",
            "pageNum": 1
        }
        token = get_token()
        headers = {"Content-Type": "application/json",
                   "Authorization": token}
        method = "post"
        response = self.api_query.test_query_api(url, json, headers, method)
        jsondata = response.json()
        mylogger.info(jsondata)
        if jsondata.get("errorCode") == 0:
            mylogger.info("errorCode为0，测试通过")
        if response.status_code == 200:
            mylogger.info("status_code为200，测试通过")
        else:
            mylogger.info("测试不通过！")
        self.assertEqual(0, jsondata.get("errorCode"))
        self.assertEqual(200, response.status_code)
