# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 16:09
# @Auth: GLK
# @File: base.py
# @Software :PyCharm
import requests, unittest


Base_Url = "https://smart-uat.gtdreamlife.com:18762/api/ioc"


class Run_Main():
    def __init__(self):
        self.session = requests.Session()

    def send_post(self, url, data, json, headers):
        response = self.session.post(url=url, data=data, json=json, headers=headers)
        return response

    def send_get(self, url, params, data, headers):
        response = self.session.get(url=url, params=params, data=data, headers=headers)
        return response

    def run(self, url=None, params=None, data=None, json=None, headers=None, method=None):
        response = None
        if method == "get":
            response = self.send_get(url, params, data, headers).json()
        else:
            response = self.send_post(url, data, json, headers).json()
        return response

    def close_session(self):
        if self.session != None:
            self.session.close()





if __name__ == "__main__":
    pass
    # run = Run_Main()
    # url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/blacklist/queryBlacklist"
    # json = {
    #     "startTime": "2021-09-01",
    #     "endTime": "2021-11-16",
    #     "projectIds": "t1",
    #     "pageNum": 1
    # }
    # headers = {"Content-Type": "application/json",
    #            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoiY3JlYXRlIGJ5IEdyZWVudG93biIsInVzZXJfaWQiOjI2OSwidXNlcl9uYW1lIjoiZ2FvbG9uZ2thaSIsInNjb3BlIjpbInNlcnZlciJdLCJlcnJvckNvZGUiOjAsImV4cCI6MTYzNzMwNTIwNiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiJdLCJqdGkiOiJhZjcxZjZiMS1iMDUwLTRiNGUtODI1Ni1kNDNiNDhiNWZiNGIiLCJjbGllbnRfaWQiOiJpb2MifQ.0mt5FCSesghL5K9Tu5-wctDPRle8sQDDcwaDQjuszu8"}
    #
    # R = run.run(url=url, json=json, headers=headers, method="post")
    # print(R)

