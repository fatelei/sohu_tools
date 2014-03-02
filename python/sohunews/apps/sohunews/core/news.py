#-*-coding: utf8-*-

import requests
import logging
import time

from sohunews.core.base import SohuNewsAPIBase
from sohunews.common.macro import SOHUNEWS_API, USER_AGENT


class SohuNewsAPINews(SohuNewsAPIBase):

    def __init__(self):
    	self.pid = "5841771463635808312"
    	self.gid = "02ffff11061111ef90d4ea6bf9f4c1c59fb44da709fd1a"
    	self.p1 = "NTg0MTcyMTEwOTY4NjY5MzkzMg%3D%3D"
        self.api = "news"

    def custom_headers(self):
        headers = {}
        headers["User-Agent"] = USER_AGENT
        headers["Content-Type"] = "text/plain; charset=ISO-8859-1"
        return headers

    def execute(self, method, uri, headers):
        try:
            func = getattr(requests, method)
            resp = func(uri, headers=headers)
            return resp
        except Exception as e:
            raise e

    def get(self, channelId, token=None):
        uri = SOHUNEWS_API[self.api]
        visitTime = int(time.time() * 1000)
        url = uri.format(channelId, visitTime, self.p1, self.gid, self.pid)
        if token:
        	url += "&token=" + token

        headers = self.custom_headers()
        resp = self.execute("get", url, headers)
        return resp.json()

if __name__ == "__main__":
    client = SohuNewsAPINews()
    resp = client.get(1)
    print resp
