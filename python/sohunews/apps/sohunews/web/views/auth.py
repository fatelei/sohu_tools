#-*-coding: utf8-*-

'''
sohu news auth
'''

import json

from tornado import gen


from sohunews.core.auth import SohuNewsAPIOAuth


from .base import BaseHandler


class SoHuNewsAuthHandler(BaseHandler):

    @gen.coroutine
    def post(self):
        email = self.get_argument("email", None)
        password = self.get_argument("password", None)
        auth_info = yield gen.Task(self.auth_user, email, password)
        self.set_secure_cookie("token", auth_info['token'])
        self.set_secure_cookie("userid", auth_info['user_id'])
        self.write(json.dumps({"login": True, "user_id": auth_info['user_id']}))

    def auth_user(self, email, password, callback):
        auth = SohuNewsAPIOAuth()
        auth_info = auth.post(email, password)
        return callback(auth_info)
