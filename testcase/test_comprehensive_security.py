# _*_ coding: utf-8 _*_
# @Time : 2021/11/26 13:59
# @Auth: GLK
# @File: test_comprehensive_security.py
# @Software :PyCharm

import unittest
from api.Comprehensive_security_api import Comprehensive_Security_Api
from base.base import Run_Main
from config.config import Logger, get_data,write_excel
from parameterized.parameterized import parameterized
from util import BASE_URL, BASE_DIR, get_token
from api.carTraffic_api import CarTraffic_Api
import warnings

mylogger = Logger(logger="Test_Comprehensive_Security_Api").getlog()
path = BASE_DIR + "/database/Comprehensive_security.xlsx"
actual_code_list = []
actual_status_list = []
result_list = []


class Test_Comprehensive_Security_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mylogger.info("开始测试Test_Comprehensive_Security_Api")
        cls.C_security_api = Comprehensive_Security_Api()

        # cls.run = Run_Main()

    @classmethod
    def tearDownClass(cls) -> None:
        write_excel(path, actual_code_list, actual_status_list, result_list)
        mylogger.info("结束测试Test_Comprehensive_Security_Api")

    def setUp(self) -> None:
        self.run = Run_Main()
        mylogger.info("开始执行测试用例")
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.run.close_session()
        mylogger.info("执行完成1条测试用例")

    @parameterized.expand(x[:-3] for x in get_data(path))
    def test_C_security_api(self, case_name, api, request_body, headers, method, expect_code, status_code):
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
        response = self.C_security_api.comprehensive_security_api(url=url, json=request_body, headers=headers,
                                                                  method=method)
        jsondata = response.json()
        actual_code = jsondata.get("errorCode")
        actual_status = response.status_code
        if expect_code == jsondata.get("errorCode") and status_code == response.status_code:
            mylogger.info(jsondata)
            mylogger.info("errorCode为{},status_code为{}".format(actual_code, actual_status))
            result = "Pass"
            mylogger.info("测试通过")
        else:
            mylogger.error("errorCode为{},status_code为{}".format(actual_code, actual_status))
            mylogger.error("测试不通过！")
            mylogger.error(jsondata)
            result = "Fail"
        actual_code_list.append(actual_code)
        actual_status_list.append(actual_status)
        result_list.append(result)
        self.assertEqual(expect_code, jsondata.get("errorCode"))
        self.assertEqual(status_code, response.status_code)

