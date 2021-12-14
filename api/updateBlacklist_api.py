# _*_ coding: utf-8 _*_
# @Time : 2021/12/13 17:12
# @Auth: GLK
# @File: updateBlacklist_api.py
# @Software :PyCharm
"""重点人员更新接口封装"""
from base.base import Run_Main


class Api_UpdateBlacklist:
    def __init__(self):
        self.run = Run_Main()

    def test_updateBlacklist_api(self, url, json, headers, method):
        return self.run.run(url=url, json=json, headers=headers, method=method)
