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

lock = threading.Lock()


def timer(func):
    def warpper(arg):
        print arg
        a = datetime.datetime.now
        c = a()
        res = func(arg)
        print a() - c
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
    pass
