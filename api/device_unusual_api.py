# _*_ coding: utf-8 _*_
# @Time : 2021/11/29 15:08
# @Auth: GLK
# @File: device_unusual_api.py
# @Software :PyCharm
from base.base import Run_Main

class Device_Unusual_Api():
    """
    设备异常告警接口
    """
    def __init__(self):
        self.run = Run_Main()

    def device_unusual_api(self,url,json,headers,method):
        return self.run.run(url=url,json=json,headers=headers,method=method)
