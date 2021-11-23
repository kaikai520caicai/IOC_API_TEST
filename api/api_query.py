# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 14:33
# @Auth: GLK
# @File: api_query.py
# @Software :PyCharm
"""重点人员查询接口封装"""
from base.base import Run_Main
from util import get_token


class Api_Query:
    def __init__(self):
        self.run = Run_Main()
        # self.url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/blacklist/queryBlacklist"
        # self.query_api_url = None
        # self.json = None
        # self.headers = None
        # self.method=None

    def test_query_api(self, url, json, headers, method):
        return self.run.run(url=url, json=json, headers=headers, method=method)


if __name__ == "__main__":
    a = Api_Query()
    url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/blacklist/queryBlacklist"
    json = {
        "name": "测试api"
    }
    token = get_token()
    headers = {"Content-Type": "application/json",
               "Authorization": token}
    method = "post"

    print(a.test_query_api(url, json, headers, method))
