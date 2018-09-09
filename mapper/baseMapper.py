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
            logger.warn("与初始模型不是同一模型")
            raise TypeError
        command = self.baseRelation['insert']
        command = command.replace('table_name', model.__class__.__name__)
        key = self.buildKey(self.relation.values())
        value = self.buildValue(model.__dict__.values())
        command = command.replace('keys', key)
        command = command.replace('values', value)
        print command

        self.cur.execute(command)
        self.conn.commit()

    def insertModels(self, models):
        if not isinstance(models, list) and not isinstance(models, tuple):
            logger.warn('必须使用可迭代类型')
            raise TypeError
        elif len(models) == 0:
            logger.warn('不能使用长度为0的iter')
            raise ValueError

        command = self.baseRelation['insert']
        res = []
        for i in models:
            t = []
            for s in i.__dict__.values():
                if isinstance(s, str):
                    s = s.decode('utf-8')
                t.append(s)
            res.append(t)

        key = self.buildKey(self.relation.values())
        value = ''
        value += '?,' * len(self.relation)
        value = value[:-1]

        command = command.replace('table_name', self.baseModel.__class__.__name__)
        command = command.replace('keys', key)
        command = command.replace('values', value)

        self.cur.executemany(command, res)
        self.conn.commit()




