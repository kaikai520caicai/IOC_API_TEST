# _*_ coding: utf-8 _*_
# @Time : 2021/11/30 13:41
# @Auth: GLK
# @File: Convenient_access_api.py
# @Software :PyCharm
from base.base import Run_Main

class Convenient_Access_Api():
    """
    便捷通行接口
    """
    def __init__(self):
        self.run = Run_Main()

    def convenient_access_api(self,url,params,headers,method):
        return self.run.run(url=url,params=params,headers=headers,method=method)