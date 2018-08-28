# -*- encoding:utf-8 -*-

import os
import re
import env


# 获取本地的map id
class localmapid():
    def __init__(self):
        self.dic = env.value('local_osu_file')
        self.maps = []

    # 格式化获取的文件夹的名字，剥离出id
    def formatid(self, str):
        str = str.split(' ')
        res = re.search('[0-9]{4,}', str[0])
        if res is None:
            return None
        return res.group(0)

    # 获取本地的mapid 返回maps[list]
    def getloaclmap(self):
        pathdir = None

        try:
            pathdir = os.listdir(self.dic)
        except WindowsError:
            print "请填写正确的osu路径"
            exit()

        for i in pathdir:
            t = i.split(' ')
            t = self.formatid(t[0])
            if t is not None:
                self.maps.append(int(t))

        return self.maps


if __name__ == '__main__':
    pass

