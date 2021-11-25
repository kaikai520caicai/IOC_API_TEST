# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 10:14
# @Auth: GLK
# @File: util.py
# @Software :PyCharm
import os
from api.login import Login_Api

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_token():

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic aW9jOmlvYw=="}
    url = "https://smart-uat.gtdreamlife.com:18762/api/auth/oauth/token"
    json = {"username": "gaolongkai", "password": "b4f1971a4d64defc3cd3f337fdc1007c", "grant_type": "password"}
    method = "post"
    login = Login_Api()
    jsondata = login.login_api(url=url, data=json, headers=headers, method=method).json()
    access_token = jsondata.get("access_token")
    Authorization = "Bearer " + access_token
    return Authorization




if __name__ == "__main__":
    token = get_token()
    print(token)
