# -*- encoding: utf-8 -*-

import requests
from maps import maps
from urllib import quote, unquote
import sys
import re
import shelve
import Queue
import threading
import time
import env

userData = {
        'username': env.value('username'),
        'password': env.value('userpassword')
    }


def getDownloadTitle(DlUrl):
    matchTitle = re.findall(r'fs=.*?&', DlUrl)
    matchTitle = ''.join(matchTitle)
    return matchTitle[3:-1]


def downloadMap(downloadUrl, userCookies):
    r = requests.get(downloadUrl, stream=True, cookies=userCookies)
    print r.url

    totalSize = int(r.headers['Content-Length'])
    tempSize = 0

    print totalSize
    downloadTitle = getDownloadTitle(unquote(r.url))

    with open(downloadTitle, 'ab') as c:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                tempSize += len(chunk)
                c.write(chunk)
                c.flush()

                done = int(50 * tempSize / totalSize)
                print "%d%%" % int(100 * tempSize / totalSize)


def bulidDownloadUrl(mapID):
    downloadUrl = 'https://osu.ppy.sh/beatmapsets/%s/download'
    return downloadUrl % mapID


def getLoginSession():
    Login_url = 'https://osu.ppy.sh/session'

    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    s = requests.session()
    # 获取用户的session
    res = s.post(Login_url, data=userData, headers=http_header)
    return res


if __name__ == '__main__':
    mapID = []
    map = maps()
    mapQueue = Queue.Queue()
    t = getLoginSession()
    userCookies = t.cookies

    if not userCookies:
        res = getLoginSession()
        db = shelve.open('userData.db')
        db['userCookies'] = res.cookies
        userCookies = res.cookies
        db.close()

    for i in range(100):
        mapID.extend(map.get(i + 1))

    for i in mapID:
        mapQueue.put(i)

    while not mapQueue.empty():
        if threading.active_count() != 5:
            t = threading.Thread(target=downloadMap, args=(bulidDownloadUrl(mapQueue.get()), userCookies))
            t.start()
        else:
            time.sleep(1)
            pass
