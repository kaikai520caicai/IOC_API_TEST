# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 14:04
# @Auth: GLK
# @File: queryBlacklist.py
# @Software :PyCharm
import requests
session=requests.Session()
url="https://smart-uat.gtdreamlife.com:18762/api/ioc/blacklist/queryBlacklist"
json={
    "startTime": "2021-09-01",
    "endTime": "2021-11-16",
    "projectIds": "t1",
    "pageNum": 1
}
headers = {"Content-Type": "application/json",
           "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoiY3JlYXRlIGJ5IEdyZWVudG93biIsInVzZXJfaWQiOjI2OSwidXNlcl9uYW1lIjoiZ2FvbG9uZ2thaSIsInNjb3BlIjpbInNlcnZlciJdLCJlcnJvckNvZGUiOjAsImV4cCI6MTYzNzEzNTkyNSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiJdLCJqdGkiOiIxMDI1ODY3Ny05ZTBjLTQ3MGEtYTUyNC1kMjUzODkyYmMzODIiLCJjbGllbnRfaWQiOiJpb2MifQ.9JpvJYvpwVaZKKzrzlNqqNz7uzRc9pgr4cB02vg5JX8"}

response=session.post(url=url,headers=headers,json=json)
print(response.json())
