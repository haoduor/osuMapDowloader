import os
import re
import shelve
import env

dic = env.value('local_osu_file')

class localmapid():
    def __init__(self):
        pass

    def formatid(str):
        str = str.split(' ')
        res = re.search('[0-9]{4,}', str[0])
        if res is None:
            return None
        return res.group(0)


if __name__ == '__main__':
    pathDir = os.listdir(dic)
    for i in pathDir:
        t = i.split(' ')
        t = re.search('[0-9]{4,}', t[0])
        if t is not None:
            print t.group(0)
