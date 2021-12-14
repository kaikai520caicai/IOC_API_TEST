# _*_ coding: utf-8 _*_
# @Time : 2021/11/29 15:11
# @Auth: GLK
# @File: test_device_unusual_api.py
# @Software :PyCharm


import unittest
from api.device_unusual_api import Device_Unusual_Api
from base.base import Run_Main
from config.config import Logger, get_data,write_excel
from parameterized.parameterized import parameterized
from util import BASE_URL, BASE_DIR, get_token
import warnings

mylogger = Logger(logger="Test_Device_Unusual_Api").getlog()
path = BASE_DIR + "/database/device_unusual.xlsx"
actual_code_list = []
actual_status_list = []
result_list = []


class Test_Device_Unusual_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mylogger.info("开始测试Test_Device_Unusual_Api")
        cls.device_unusual_api = Device_Unusual_Api()

        # cls.run = Run_Main()

    @classmethod
    def tearDownClass(cls) -> None:
        write_excel(path, actual_code_list, actual_status_list, result_list)
        mylogger.info("结束测试Test_Device_Unusual_Api")

    def setUp(self) -> None:
        self.run = Run_Main()
        mylogger.info("开始执行测试用例")
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.run.close_session()
        mylogger.info("执行完成1条测试用例")

    @parameterized.expand(x[:-3] for x in get_data(path))
    def test_device_unusual_api(self, case_name, api, request_body, headers, method, expect_code, status_code):
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
        response = self.device_unusual_api.device_unusual_api(url=url, json=request_body, headers=headers,
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
