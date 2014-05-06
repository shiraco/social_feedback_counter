# coding:utf-8

import urllib
import json


class SocialFeadbackCounter(object):
    def __init__(self, url):
        self.url = url

    def hatebu(self):
        api_url = 'http://b.hatena.ne.jp/entry/json/' + self.url
        hb_json = json.loads(urllib.urlopen(api_url).read(), encoding='utf-8')

        if hb_json is not None:
            return int(hb_json['count'])
        else:  # In case 0, response is null(None)
            return 0

    def fb_like(self):
        api_url = 'http://graph.facebook.com/' + self.url
        fb_json = json.loads(urllib.urlopen(api_url).read(), encoding='utf-8')
        try:
            return fb_json['shares']
        except KeyError:  # In case 0, 'share' key is not exsist in response json
            return 0

    def tweet(self):
        api_url = 'http://urls.api.twitter.com/1/urls/count.json?url=' + self.url
        tw_json = json.loads(urllib.urlopen(api_url).read(), encoding='utf-8')
        return tw_json['count']


if __name__ == '__main__':
    u = SocialFeadbackCounter('https://www.google.co.jp/')
    print u.hatebu(), u.fb_like(), u.tweet()
