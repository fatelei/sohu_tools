#-*-=coding: utf8-*-

import json

from tornado import gen


from sohunews.core.news import SohuNewsAPINews
from sohunews.web.views.base import BaseHandler


class SohuNewsHandler(BaseHandler):

    @gen.coroutine
    def get(self, channelId, page=1):
        news = yield gen.Task(self.get_news, channelId, page)
        try:
        	self.write(json.dumps(news['articles']))
        except:
        	self.write(json.dumps([]))

    def get_news(self, channelId, page, callback):
        sohuNewsAPINews = SohuNewsAPINews()
        news = sohuNewsAPINews.get(channelId, page=page)
        return callback(news)
