# -*- encoding:utf-8 -*-

import yaml

f = None
try:
    f = open('config.yaml')
except IOError:
    print '请不要把config.yaml删掉'
    exit('cnm听到了吗')
res = yaml.load(f)


# 从config.yaml获取环境变量
def value(v):
    return res[v]
