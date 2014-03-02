#!/usr/bin/python
#-*-coding: utf8-*-

import os
import tornado.web
import tornado.ioloop

from .urls import handlers


settings = {
    "debug": True,
    "template_path": os.path.join(os.path.dirname(__file__), "../templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "../static"),
    "cookie_secret": "asddasdasdasdasd"
}


def run():
    application = tornado.web.Application(handlers, **settings)
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
