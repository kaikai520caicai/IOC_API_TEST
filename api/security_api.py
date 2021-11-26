# _*_ coding: utf-8 _*_
# @Time : 2021/11/26 10:44
# @Auth: GLK
# @File: security_api.py
# @Software :PyCharm
from base.base import Run_Main


class Security_Api():
    """
    1.	园区态势-综合态势
    1)	近一周安防管理-安防实况
    2)  近一周安防管理-事件类型

    """

    def __init__(self):
        self.run = Run_Main()

    def security_api(self, url, headers, method):
        return self.run.run(url=url, headers=headers, method=method)
