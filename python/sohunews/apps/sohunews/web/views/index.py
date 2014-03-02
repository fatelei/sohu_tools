#-*-coding: utf8-*-

from .base import BaseHandler


class SohuNewsIndexHandler(BaseHandler):

	def get(self):
		self.render("index.html")
