#-*-coding: utf8-*-


class SohuNewsAPIBase(object):

    def __init__(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def custom_headers(self):
        raise NotImplementedError
