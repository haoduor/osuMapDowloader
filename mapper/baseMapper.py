# -*- encoding:utf-8 -*-

import yaml
import log
from sqlite import sql

logger = log.getlogger()


class baseMapper:
    def __init__(self, model=None):
        self.baseModel = model
        self.relation = self.loadConf(model)
        self.baseRelation = self.loadConf()
        self.conn = sql().getConn()
        self.cur = self.conn.cursor()

    def loadConf(self, model=None):
        path = 'mapper/mapper/%s.yaml' % self.__class__.__name__
        if model:
            path = 'mapper/mapper/%sMapper.yaml' % model.__class__.__name__
        with open(path) as f:
            res = yaml.load(f)
        return res

    @staticmethod
    def buildKey(iterStr):
        res = ''
        for i in iterStr:
            res += str(i)+','
        return res[:-1]

    @staticmethod
    def buildValue(iterStr):
        res = ''
        for i in iterStr:
            if isinstance(i, str):
                i = '\'%s\'' % i
            res += str(i) + ','

        return res[:-1]

    def insertModel(self, model):
        if not isinstance(model, self.baseModel.__class__):
            # TODO 补全异常
            logger.warn("与初始模型不是同一模型")
            raise Exception
        com = self.baseRelation['insert']
        com = com.replace('table_name', model.__class__.__name__)
        key = self.buildKey(self.relation.values())
        value = self.buildValue(model.__dict__.values())
        com = com.replace('keys', key)
        com = com.replace('values', value)
        print com

        self.cur.execute(com)
        self.conn.commit()

        self.cur.close()

    def insertModels(self, model):
        pass
