import os
import re
import shelve
import env



class localmapid():
    def __init__(self):
        self.dic = env.value('local_osu_file')
        self.maps = []

    def formatid(self, str):
        str = str.split(' ')
        res = re.search('[0-9]{4,}', str[0])
        if res is None:
            return None
        return res.group(0)

    def getloaclmap(self):
        pathdir = os.listdir(self.dic)
        for i in pathdir:
            t = i.split(' ')
            t = self.formatid(t[0])
            if t is not None:
                self.maps.append(int(t))

        return self.maps


if __name__ == '__main__':
    pass

