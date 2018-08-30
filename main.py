# -*- encoding:utf-8 -*-

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
import localmap
import datetime
from db import data

userData = env.value('userdata')

downloadUrl = env.value('downloadUrl')


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
                print "%s %d%%" % (downloadTitle, int(100 * tempSize / totalSize))


def buildDownloadUrl(mapID):
    return downloadUrl % mapID


def getLoginSession():
    loginUrl = env.value('loginUrl')

    httpHeader = env.value('User-Agent')

    s = requests.session()
    # 获取用户的session id
    res = s.post(loginUrl, data=userData, headers=httpHeader)
    return res.cookies


def testUserCookies(usercookies):
    r = requests.get(downloadUrl % '123456', cookies=usercookies)
    try:
        a = r.headers['Content-Disposition']
        return True
    except:
        return False


if __name__ == '__main__':
    # 开启用户的数据库
    userDB = data('userData.db')
    # 开启map的数据库
    mapBD = data('map.db')
    # 存放要下载的map id
    mapID = []
    # 从网络获取mpa id
    map = maps()
    # 要下载的地图队列
    mapQueue = Queue.Queue()
    # 从数据库中获取已经登陆的用户session id
    userCookies = userDB.get('userCookies')
    # 从数据库中获取用户session id的过期时间
    # 过期时间1天
    userCookiesExpiryTime = userDB.get('userCookiesExpiryTime')

    # 判断是用户session id是否为空，用户session id是否过期
    if userCookies is None or userCookiesExpiryTime < datetime.datetime.now():
        # 重新获取用户的cookies
        userCookies = getLoginSession()
        # 设置用户cookies的过期时间
        userCookiesExpiryTime = datetime.datetime.now() + datetime.timedelta(1)
        # 覆盖数据库
        userDB.insert('userCookies', userCookies)
        userDB.insert('userCookiesExpiryTime', userCookiesExpiryTime)

    '''
        userData.db:
            userCookies: 用户的cookies
            userCookiesExpiryTime： cookies的过期时间
            
        maps.db:
            Imaps: 所有从网络获取的id
            Lmaps: 本地的id
    '''

    for i in range(100):
        mapID.extend(map.get(i + 1))

    for i in mapID:
        mapQueue.put(i)

    while not mapQueue.empty():
        if threading.active_count() != 5:
            t = threading.Thread(target=downloadMap, args=(buildDownloadUrl(mapQueue.get()), userCookies))
            t.start()
        else:
            time.sleep(1)
            pass
