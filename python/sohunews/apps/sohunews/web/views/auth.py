#-*-coding: utf8-*-

'''
sohu news auth
'''

from tornado import gen


from sohunews.core.auth import SohuNewsAPIOAuth


from .base import BaseHandler


class SoHuNewsAuthHandler(BaseHandler):

	@gen.coroutine
	def post(self):
		email = self.get_argument("email", None)
		password = self.get_argument("password", None)

		auth_info = yield gen.Task(self.auth_user, email, password)

		self.write({"login": True})

	def auth_user(self, email, password, callback):
		auth = SohuNewsAPIOAuth()
		auth_info = auth.post(email, password)
		return callback(auth_info)