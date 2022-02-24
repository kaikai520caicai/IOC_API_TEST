# _*_ coding: utf-8 _*_
# @Time : 2022/2/24 16:48
# @Auth: GLK
# @File: ioc_config_api.py
# @Software :PyCharm

"""重点人员查询接口封装"""
from base.base import Run_Main
from util import get_token


class Api_Ioc_config:
    def __init__(self):
        self.run = Run_Main()
        # self.url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/blacklist/queryBlacklist"
        # self.query_api_url = None
        # self.json = None
        # self.headers = None
        # self.method=None

    def test_ioc_config_api(self, url, json, headers, method):
        return self.run.run(url=url, json=json, headers=headers, method=method)



