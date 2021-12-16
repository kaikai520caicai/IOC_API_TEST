# _*_ coding: utf-8 _*_
# @Time : 2021/12/1 11:05
# @Auth: GLK
# @File: uploadPersonPic_api.py
# @Software :PyCharm
from base.base import Run_Main
# from util import get_token,BASE_DIR
import requests


from requests_toolbelt import MultipartEncoder


class UploadPersonPic_Api():
    """
    重点人员人脸上传接口
    """

    def __init__(self):
        self.run = Run_Main()

    def uploadPersonPic_api(self, url, headers, files, method):
        return self.run.run(url=url, headers=headers, files=files, method=method)


# if __name__ == "__main__":
#     url = "https://smart-uat.gtdreamlife.com:18762/api/ioc/personTrack/uploadPersonPic"
#     path = BASE_DIR + "\\" + "test.jpg"
#     print(path)
#
#
#     token = get_token()
#     headers = {"Authorization": token}
#     files = {'file': ("test.jpg", open(path, "rb"), "image/jpeg", {})}
#     method = "post"
#     U = UploadPersonPic_Api()
#     response = U.uploadPersonPic_api(url, headers, files, method)
#     print(response.json())
