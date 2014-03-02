#-*-coding: utf8-*-

"""
sohu news app auth
"""

import requests
import logging

from hashlib import md5

from sohunews.core.base import SohuNewsAPIBase
from sohunews.common.macro import SOHUNEWS_API, USER_AGENT
from sohunews.utils.params import generate_params


class SohuNewsAPIOAuth(SohuNewsAPIBase):

    def __init__(self):
        self.gid = "02ffff11061111ef90d4ea6bf9f4c1c59fb44da709fd1a"
        self.sig = "a622b02686a27feb456dc856e7d81fdd"
        self.appid = "1106"
        self.api = "login"

    def custom_headers(self):
        headers = {}
        headers["User-Agent"] = USER_AGENT
        headers["Content-Type"] = "text/plain; charset=ISO-8859-1"
        return headers

    def execute(self, method, uri, data, headers):
        try:
            func = getattr(requests, method)
            resp = func(uri, headers=headers, data=data)
            return resp
        except Exception as e:
            logging.warning(e)

    def convert_to_json(self):
        pass

    def post(self, userid, password):
        uri = SOHUNEWS_API[self.api]
        self.userid = userid

        # 需要对密码进行md5加密
        md = md5()
        md.update(password)
        self.password = md.hexdigest()
        data = generate_params(self)
        headers = self.custom_headers()
        resp = self.execute("post", uri, data, headers)
        return resp


if __name__ == "__main__":
    client = SohuNewsAPIOAuth()
    resp = client.post("fate_lei@sohu.com", "fate123")
    print resp.status_code
    print resp.text

