# -*- encoding:utf-8 -*-

from model import maps
from sqlite import sql

'''
 完成maps的数据库映射
 insert
 deleteById
 updateById
 selectById
 selectByName
 selectByTime
'''

cur = sql().getCur()


class mapsMapper():
    def __init__(self):
        pass

    def insertMaps(self, maps):
        pass
