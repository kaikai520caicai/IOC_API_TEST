# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 10:14
# @Auth: GLK
# @File: util.py
# @Software :PyCharm
import os
from api.login import Login_Api
from api.uploadPersonPic_api import UploadPersonPic_Api
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_URL = "https://smart-uat.gtdreamlife.com:18762"
BASE_URL = "https://smart.gtdreamlife.com:18762"


def get_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic aW9jOmlvYw=="}
    url = "https://smart.gtdreamlife.com:18762/api/auth/oauth/token"
    json = {"username": "gaolongkai", "password": "b4f1971a4d64defc3cd3f337fdc1007c", "grant_type": "password"}
    method = "post"
    login = Login_Api()
    jsondata = login.login_api(url=url, data=json, headers=headers, method=method).json()
    access_token = jsondata.get("access_token")
    Authorization = "Bearer " + access_token
    return Authorization


def get_pic(token):
    url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/personTrack/uploadPersonPic"
    path = BASE_DIR + "\\" + "test.jpg"
    headers = {"Authorization": token}
    files = {'file': ("test.jpg", open(path, "rb"), "image/jpeg", {})}
    method = "post"
    U = UploadPersonPic_Api()
    jsondata = U.uploadPersonPic_api(url, headers, files, method).json()
    data = jsondata.get("data")
    return data


def send_email(file_path):
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login("281384017@qq.com", "yknhlsvdhakbcbcf")

    smg = MIMEMultipart()
    text_smg = MIMEText("测试报告", "plain", "utf8")
    smg.attach(text_smg)

    file_msg = MIMEApplication(open(file_path, "rb").read())
    file_msg.add_header('content-disposition', 'attachment', filename='IOC接口自动化测试report.html')
    smg.attach(file_msg)

    smg["Subject"] = "IOC接口自动化测试报告"
    smg["From"] = "281384017@qq.com"
    smg["To"] = "2630322121@qq.com,k281384017@163.com"
    smtp.send_message(smg, from_addr="281384017@qq.com", to_addrs="2630322121@qq.com,k281384017@163.com")


if __name__ == "__main__":
    # token = get_token()
    # print(token)
    # pic = get_pic()
    # print(pic)
    path = r"D:\IOC_Api_Test\report\20211215170839测试报告.html"
    send_email(path)
