#-*-coding: utf8-*-

'''
get all channels from sohu news
'''

import json

from tornado import gen

from sohunews.web.views.base import BaseHandler
from sohunews.core.channel import SohuNewsAPIChannel

class SohuNewsChannelsHandler(BaseHandler):

	@gen.coroutine
	def get(self):
		channels = yield gen.Task(self.get_channels)
		self.write(json.dumps(channels))

	def get_channels(self, callback):
		sohuNewsAPIChannel = SohuNewsAPIChannel()
		channels = sohuNewsAPIChannel.get()
		return callback(channels)
	
