#-*-coding: utf8-*-

from sohunews.web.views import auth
from sohunews.web.views import channel
from sohunews.web.views import index
from sohunews.web.views import news
from sohunews.web.views import articles

handlers = [
    (r'/', index.SohuNewsIndexHandler),
    (r'/channles', channel.SohuNewsChannelsHandler),
    (r'/login', auth.SoHuNewsAuthHandler),
    (r'/news/(\d+)/(\d+)', news.SohuNewsHandler),
    (r'/articles', articles.SohuNewsArticleHandler)
]
