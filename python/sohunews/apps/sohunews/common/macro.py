#-*-coding: utf8-*-


"""
sohunews macro
"""

SOHUNEWS_API = {
    "login": "https://passport.sohu.com/mobile/gettoken",
    "channel": "http://api.k.sohu.com/api/channel/list.go?supportLive={0}&supportWeibo={1}&refer={2}&p1={3}&gid={4}&pid={5}",
    "news": "http://api.k.sohu.com/api/channel/v4/news.go?channelId={0}&num=20&page={1}&imgTag=1&showPic=1&picScale=2&rt=json&pull=0&visitTime={2}&more=0&lastPullTime=0&net=wifi&from=channel&p1={3}&gid={4}&pid={5}",
}

USER_AGENT = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"


