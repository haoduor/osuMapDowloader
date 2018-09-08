# -*- encoding:utf-8 -*-

from model import maps
from baseMapper import baseMapper

'''
 完成maps的数据库映射
 insert
 deleteById
 updateById
 selectById
 selectByName
 selectByTime
'''


class mapsMapper(baseMapper):
    def __init__(self):
        baseMapper.__init__(self, maps())

    def insertMaps(self, maps):
        pass

    def getName(self):
        print self.__class__.__name__
