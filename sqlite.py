# -*- encoding:utf-8 -*-

import sqlite3
import env

# 使用sqlite数据库对map和beatmap的数据进行持久化
# 类可以获取sql的指针对象


class sql():
    sql_name = env.value('sqlname')
    _cur = None

    def __init__(self):
        self.conn = sqlite3.connect(self.sql_name)
        self._cur = self.conn.cursor()
        pass

    def getCur(self):
        return self._cur
