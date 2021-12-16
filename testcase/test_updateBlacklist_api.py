# _*_ coding: utf-8 _*_
# @Time : 2021/12/13 17:15
# @Auth: GLK
# @File: test_updateBlacklist_api.py
# @Software :PyCharm

import requests
from api.updateBlacklist_api import Api_UpdateBlacklist
from base.base import Run_Main
import unittest, time
import warnings
from parameterized import parameterized
from config.config import get_data, write_excel, Clear_excel
from util import BASE_DIR, BASE_URL, get_token,get_pic
from config.config import Logger

mylogger = Logger(logger="test_updateBlacklist_api").getlog()

actual_code_list = []
actual_status_list = []
result_list = []
path = BASE_DIR + "/database/updateBlacklist.xlsx"


class Test_Api_UpdateBlacklist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mylogger.info("开始测试Test_Api_UpdateBlacklist")
        cls.updateBlacklist_api = Api_UpdateBlacklist()

        # cls.run = Run_Main()

    @classmethod
    def tearDownClass(cls) -> None:
        write_excel(path, actual_code_list, actual_status_list, result_list)
        mylogger.info("结束测试Test_Api_UpdateBlacklist")

    def setUp(self) -> None:
        self.run = Run_Main()
        mylogger.info("开始执行测试用例")
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.run.close_session()
        mylogger.info("执行完成1条测试用例")

    @parameterized.expand(x[:-3] for x in get_data(path))
    def test_updateBlacklist_api(self, case_name, api, request_body, headers, method, expect_code, status_code):
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
        #上传人脸接口，获取人脸url
        facepic = get_pic(token)
        headers["Authorization"] = token
        mylogger.info(headers)
        request_body["facePic"] = facepic
        response = self.updateBlacklist_api.test_updateBlacklist_api(url=url, json=request_body, headers=headers,
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

