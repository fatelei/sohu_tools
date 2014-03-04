#-*-coding: utf8-*-

import urlparse
import urllib

from tornado import gen
from tornado.web import HTTPError

from sohunews.core.article import SohuNewsAPIArticle
from sohunews.web.views.base import BaseHandler


class SohuNewsArticleHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        CDN_URL = self.get_argument("CDN_URL", None)
        if CDN_URL:
            real_url = self.parse_url(CDN_URL)
            data = yield gen.Task(self.get_article, real_url)

            user = self.get_current_user()
            user_info = {}
            if user:
                user_info['userid'] = user
            self.render("article.html", data=data, user_info=user_info)
        else:
            raise HTTPError(404)

    def parse_url(self, url):
        real_url = urllib.unquote(url)
        return real_url

    def get_article(self, url, callback):
        sohuNewsAPIArticle = SohuNewsAPIArticle()
        data = sohuNewsAPIArticle.get(url)
        return callback(data)
