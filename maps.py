# -*- encoding:utf-8 -*-

import requests
import env
import datetime


def timer(func):
    def wrapper(self, *arg, **kwargs):
        now = datetime.datetime.now
        before = now()
        res = func(self, *arg, **kwargs)
        print 'finish', now() - before, '  pages=', arg[0]
        return res
    return wrapper


# 从网络批量获取map id
class maps(object):
    def __init__(self):
        self.defaultMapUrl = env.value('mapapi')
        self.old = env.value('sourceTemp')
        self.buildMapUrl = ''
        # self.pattern = {
        #     'mode': 'm',
        #     'Rank status': 'r',
        #     'Genre': 'g',
        #     'Language': 'l',
        # }
        self.setUrl()

    def setpattern(self, **args):
        pass

    # 从环境中获取设置的url，并合成map api
    def setUrl(self):
        temp = env.value('sourceUrl')
        temp = temp.replace(self.old, self.defaultMapUrl)
        self.buildMapUrl = temp

    # 使用设置的api来获取map id
    @timer
    def get(self, pages=1):
        mapsID = []
        DUrl = self.buildMapUrl + '&page=' + str(pages)

        r = requests.get(DUrl)
        res = r.json()
        if not res:
            return None

        for i in range(len(res)):
            mapsID.append(res[i]['id'])
        return mapsID


