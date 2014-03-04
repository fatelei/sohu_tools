#-*-coding: utf8-*-

from .base import BaseHandler


class SohuNewsIndexHandler(BaseHandler):

    def get(self):
        user = self.get_current_user()
        user_info = {}
        if user:
            user_info['userid'] = user

        print user_info
        self.render("index.html", user_info=user_info)
