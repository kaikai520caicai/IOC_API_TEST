# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 10:14
# @Auth: GLK
# @File: util.py
# @Software :PyCharm
import os
from api.login import Login_Api
from api.uploadPersonPic_api import UploadPersonPic_Api

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://smart-uat.gtdreamlife.com:18762"


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


def get_pic():
    url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/personTrack/uploadPersonPic"
    path = BASE_DIR + "\\" + "test.jpg"
    token = get_token()
    headers = {"Authorization": token}
    files = {'file': ("test.jpg", open(path, "rb"), "image/jpeg", {})}
    method = "post"
    U = UploadPersonPic_Api()
    jsondata = U.uploadPersonPic_api(url, headers, files, method).json()
    data = jsondata.get("data")
    return data


if __name__ == "__main__":
    token = get_token()
    print(token)
    # pic = get_pic()
    # print(pic)
