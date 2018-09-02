# -*- encoding:utf-8 -*-

import yaml

# 用于从本地的yaml文件中获取环境变量
# 适用于只读型变量，yaml中的变量尽量不要更改

f = None
try:
    f = open('config.yaml')
except IOError:
    print '请不要把config.yaml删掉'
    exit('cnm听到了吗')
res = yaml.load(f)
f.close()


# 从config.yaml获取环境变量
def value(v):
    return res[v]
