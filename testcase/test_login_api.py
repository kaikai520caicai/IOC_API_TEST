# _*_ coding: utf-8 _*_
# @Time : 2021/11/22 13:17
# @Auth: GLK
# @File: test_login_api.py
# @Software :PyCharm
from api.login import Login_Api
from base.base import Run_Main
import unittest, time
import warnings
from parameterized import parameterized
from config.config import get_data, write_excel, Clear_excel
from util import BASE_DIR
from config.config import Logger

mylogger = Logger(logger="test_query_api").getlog()

actual_code_list = []
actual_status_list = []
result_list = []
path = BASE_DIR + "/database/login_data.xlsx"
# clsclear = Clear_excel()
# clsclear.get_nrows(path)

class Test_Login_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mylogger.info("----------------开始测试登录接口---------------")

    @classmethod
    def tearDownClass(cls):
        write_excel(path, actual_code_list, actual_status_list, result_list)
        mylogger.info("----------------登录接口测试结束---------------")

    def setUp(self) -> None:
        mylogger.info("--------开始执行测试用例--------")
        self.login = Login_Api()
        self.run = Run_Main()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        mylogger.info("-------结束执行1条测试用例---------")
        self.run.close_session()

    @parameterized.expand([x[:-3] for x in get_data(path)])
    def test_login(self, case_name, url, json, method, expect_code, status_code):
        """

        :param case_name:
        :param url:
        :param json:
        :param method:
        :param expect:
        :return:
        """
        mylogger.info(case_name)
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic aW9jOmlvYw=="}
        response = self.login.login_api(url=url, data=json, headers=headers, method=method)
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
