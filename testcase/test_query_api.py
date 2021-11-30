# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 14:40
# @Auth: GLK
# @File: test_query_api.py
# @Software :PyCharm
import requests
from api.api_query import Api_Query
from base.base import Run_Main
import unittest, time
import warnings
from parameterized import parameterized
from config.config import get_data, write_excel, Clear_excel
from util import BASE_DIR, BASE_URL, get_token
from config.config import Logger

mylogger = Logger(logger="test_query_api").getlog()

actual_code_list = []
actual_status_list = []
result_list = []
path = BASE_DIR + "/database/queryBlacklist.xlsx"


class Test_Api_Query(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mylogger.info("开始测试Test_Api_Query")
        cls.query_api = Api_Query()

        # cls.run = Run_Main()

    @classmethod
    def tearDownClass(cls) -> None:
        mylogger.info("结束测试Test_Api_Query")

    def setUp(self) -> None:
        self.run = Run_Main()
        mylogger.info("开始执行测试用例")
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.run.close_session()
        mylogger.info("执行完成1条测试用例")

    @parameterized.expand(x[:-3] for x in get_data(path))
    def test_fire_and_security_api(self, case_name, api, request_body, headers, method, expect_code, status_code):
        """

        :param case_name:
        :param api:
        :param headers:
        :param method:
        :param expect_code:
        :param status_code:
        :return:
        """
        mylogger.info("测试用例名称：{}".format(case_name))
        url = BASE_URL + api
        mylogger.info("url为：{}".format(url))
        token = get_token()
        headers["Authorization"] = token
        response = self.query_api.test_query_api(url=url, json=request_body, headers=headers,
                                                 method=method)
        jsondata = response.json()
        actual_code = jsondata.get("errorCode")
        actual_status = response.status_code
        mylogger.info(jsondata)
        if expect_code == jsondata.get("errorCode"):
            mylogger.info("errorCode为{},测试通过".format(expect_code))
        if status_code == response.status_code:
            mylogger.debug("status_code为{},测试通过".format(status_code))
            result = "Pass"
        else:
            mylogger.info("测试不通过！")
            result = "Fail"
        self.assertEqual(expect_code, jsondata.get("errorCode"))
        self.assertEqual(status_code, response.status_code)
        actual_code_list.append(actual_code)
        actual_status_list.append(actual_status)
        result_list.append(result)
