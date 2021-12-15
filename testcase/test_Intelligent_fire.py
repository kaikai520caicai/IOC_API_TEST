# _*_ coding: utf-8 _*_
# @Time : 2021/11/30 11:14
# @Auth: GLK
# @File: test_Intelligent_fire.py
# @Software :PyCharm


import unittest
from api.Intelligent_fire_api import Intelligent_Fire_Api
from base.base import Run_Main
from config.config import Logger, get_data,write_excel
from parameterized.parameterized import parameterized
from util import BASE_URL, BASE_DIR, get_token
import warnings

mylogger = Logger(logger="Test_Intelligent_Fire_Api").getlog()
path = BASE_DIR + "/database/Intelligent_fire.xlsx"
actual_code_list = []
actual_status_list = []
result_list = []


class Test_Intelligent_Fire_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mylogger.info("开始测试Test_Intelligent_Fire_Api")
        cls.intelligent_fire_api = Intelligent_Fire_Api()

        # cls.run = Run_Main()

    @classmethod
    def tearDownClass(cls) -> None:
        write_excel(path, actual_code_list, actual_status_list, result_list)
        mylogger.info("结束测试Test_Intelligent_Fire_Api")

    def setUp(self) -> None:
        self.run = Run_Main()
        mylogger.info("开始执行测试用例")
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.run.close_session()
        mylogger.info("执行完成1条测试用例")

    @parameterized.expand(x[:-3] for x in get_data(path))
    def test_fire_and_security_api(self, case_name, api, params, headers, method, expect_code, status_code):
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

        response = self.intelligent_fire_api.intelligent_fire_api(url=url, params=params, headers=headers,
                                                                  method=method)
        jsondata = response.json()
        actual_code = jsondata.get("errorCode")
        actual_status = response.status_code
        if expect_code == jsondata.get("errorCode") and status_code == response.status_code:
            mylogger.info(jsondata)
            mylogger.info("errorCode为{},status_code为{}".format(expect_code, status_code))
            result = "Pass"
            mylogger.info("测试通过")
        else:
            mylogger.error("errorCode为{},status_code为{}".format(expect_code, status_code))
            mylogger.error("测试不通过！")
            mylogger.error(jsondata)
            result = "Fail"
        actual_code_list.append(actual_code)
        actual_status_list.append(actual_status)
        result_list.append(result)
        self.assertEqual(expect_code, jsondata.get("errorCode"))
        self.assertEqual(status_code, response.status_code)

