# -*- encoding:utf-8 -*-

import shelve


# 连接本地的数据库可以将对象直接存储，但是没有数据库结构
# 仅用于存储的用户的cookies对象

class data(object):
    def __init__(self, filename):
        self.infor = shelve.open(filename)

    def get(self, key):
        res = None
        try:
            res = self.infor[key]
        except KeyError:
            return None
        return res

    def insert(self, key, value):
        self.infor[key] = value
