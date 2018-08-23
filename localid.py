import os
import re


def formatid(str):
    str = str.split(' ')
    res = re.search('[0-9]{4,}', str[0])
    if res is None:
        return None
    return res.group(0)


if __name__ == '__main__':
    dic = 'F:\\osu!\\Songs'
    pathDir = os.listdir(dic)
    for i in pathDir:
        t = i.split(' ')
        t = re.search('[0-9]{4,}', t[0])
        if t is not None:
            print t.group(0)


