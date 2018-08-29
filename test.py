# -*- encoding:utf-8 -*-

import sys
import time
import threading
import Queue
import shelve
import requests
import main
import os
import time
import datetime
import yaml
from db import data
from maps import maps
from localid import localmapid
import log
import logging

lock = threading.Lock()


def timer(func):
    def warpper(arg):
        print arg
        now = datetime.datetime.now
        before = now()
        res = func(arg)
        print now() - before
        return res
    return warpper


def pp(a):
    for i in range(3):
        lock.acquire()
        print a, threading.activeCount()
        lock.release()
        time.sleep(1)


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileCreateTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


@timer
def get_FileAccessTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


@timer
def aaa(a):
    time.sleep(a)


if __name__ == '__main__':
    # t = range(1, 100)
    # q = Queue.Queue()
    # for i in t:
    #     q.put(i)
    #
    # while not q.empty():
    #     if threading.active_count() != 5:
    #         t = threading.Thread(target=pp, args=(q.get(), ))
    #         t.start()
    #     else:
    #         pass
    #
    # print 'end'
    # print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)]))

    # 创建本地数据库
    # mapsData = data('maps.db')
    # map = maps()
    # localmaps = localmapid()
    # mapsDataList = []
    # localMapDataList = []
    #
    # # for i in range(1, 100):
    # #     mapsDataList.extend(map.get(i))
    # localMapDataList.extend(localmaps.getloaclmap())
    # mapsDataList = mapsData.get("Imaps")
    # mapsData.insert("Lmaps", localMapDataList)
    #
    # mapsDataList = set(mapsDataList)
    # localMapDataList = set(localMapDataList)
    #
    # DL = mapsDataList - localMapDataList
    #
    # print len(DL)
    # print DL

    a = maps()
    Imaps = []
    logger = logging.getLogger('gu')
    logger.info('asdasdasdasd')
    # temp = 0
    # while True:
    #     t = a.get(temp)
    #     if not t:
    #         break
    #     Imaps.extend(t)
    #     temp += 1
    #
    # print len(Imaps)

    pass