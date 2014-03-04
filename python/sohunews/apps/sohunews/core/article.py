#!/usr/bin/python
#-*-coding: utf8-*-

import requests

import logging

from lxml import etree

from sohunews.core.base import SohuNewsAPIBase
from sohunews.common.macro import USER_AGENT


class SohuNewsAPIArticle(SohuNewsAPIBase):

    def __init__(self):
        self.api = "article"

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

    def convert_to_json(self, resp):
        root = etree.fromstring(resp.text.encode("utf8"))
        data = {}
        data['title'] = root.xpath("//title")[0].text
        data['content'] = root.xpath("//content")[0].text
        return data

    def get(self, url):
        headers = self.custom_headers()
        resp = self.execute("get", url, headers)
        return self.convert_to_json(resp)

if __name__ == "__main__":
    client = SohuNewsAPINews()
    resp = client.get("http://zcache.k.sohu.com/api/news/cdn/v1/article.go/16633271/1/613/0/3/1/18/18/3/1/1/1393751199000.xml")
    print resp
