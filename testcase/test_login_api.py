# _*_ coding: utf-8 _*_
# @Time : 2021/11/22 13:17
# @Auth: GLK
# @File: test_login_api.py
# @Software :PyCharm
from api.login import Login_Api
from base.base import Run_Main
import unittest
import warnings
from parameterized import parameterized
from config.config import get_data
from util import BASE_DIR
from config.config import Logger

mylogger = Logger(logger="test_query_api").getlog()


class Test_Login_Api(unittest.TestCase):
    def setUp(self) -> None:
        mylogger.info("--------开始执行测试用例--------")
        self.login = Login_Api()
        self.run = Run_Main()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        mylogger.info("-------结束执行测试用例---------")
        self.run.close_session()

    @parameterized.expand(get_data(BASE_DIR + "/database/login_data.xlsx"))
    def test_login(self, case_name, url, json, method, exp):
        """

        :param case_name:
        :param url:
        :param json:
        :param method:
        :param expect:
        :return:
        """

        # json = eval(json)
        mylogger.info(case_name)
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic aW9jOmlvYw=="}
        # url = "https://smart-uat.gtdreamlife.com:18762/api/auth/oauth/token"
        # json = {"username":"gaolongkai","password":"b4f1971a4d64defc3cd3f337fdc1007c","grant_type":"password"}
        # method = "post"
        jsondata = self.login.login_api(url=url, data=json, headers=headers, method=method)
        mylogger.info(jsondata)
        if exp==jsondata.get("errorCode"):
            mylogger.info("测试通过")
        else:
            mylogger.info("测试不通过！")
        self.assertEqual(exp, jsondata.get("errorCode"))





