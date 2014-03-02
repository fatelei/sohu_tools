#-*-coding: utf8-*-

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

	def get_current_user(self):
		token = self.get_secure_cookie("sohunews_token")
		if not token:
			return None
		else:
			return token

	def get_login_url(self):
		return "/login"
