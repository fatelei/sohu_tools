#-*-coding: utf8-*-

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

	def get_current_user(self):
		userid = self.get_secure_cookie("userid")
		if not userid:
			return None
		else:
			return userid

	def get_login_url(self):
		return "/login"
