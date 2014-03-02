#-*-coding: utf8-*-

'''
sohu news channel api
'''

import requests

from lxml import etree

from sohunews.common.macro import SOHUNEWS_API, USER_AGENT

from sohunews.core.base import SohuNewsAPIBase


class SohuNewsAPIChannel(SohuNewsAPIBase):

    def __init__(self):
        self.supportLive = 1
        self.supportWeibo = 1
        self.refer = 17
        self.p1 = "NTg0MTcyMTEwOTY4NjY5MzkzMg"
        self.gid = "02ffff11061111ef90d4ea6bf9f4c1c59fb44da709fd1a"
        self.pid = "5841771463635808312"
        self.api = "channel"

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
            logging.warning(e)
            return None

    def convert_to_json(self, resp):
        xml_str = resp.text
        root = etree.fromstring(xml_str.encode("utf8"))
        children = root.xpath("//channels/channel")
        channels = []

        for child in children:
            channels.append(
                {"name": child.get("name"), "id": child.get("id"), "icon": child.get("icon")})
        return channels

    def get(self):
        uri = SOHUNEWS_API[self.api]
        headers = self.custom_headers()
        url = uri.format(
            self.supportLive, self.supportWeibo, self.refer, self.p1, self.gid, self.pid)
        resp = self.execute("get", url, headers)
        if resp:
            return self.convert_to_json(resp)
        else:
            return None

if __name__ == "__main__":
    sohuNewsAPIChannel = SohuNewsAPIChannel()
    print sohuNewsAPIChannel.get()
