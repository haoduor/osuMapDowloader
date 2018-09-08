# -*- encoding:utf-8 -*-

import yaml
import log

# 用于从本地的yaml文件中获取环境变量
# 适用于只读型变量，yaml中的变量尽量不要更改

logger = log.getlogger()

f = None
try:
    f = open('config.yaml')
except IOError:
    logger.warn('config.yaml丢失')
    exit('cnm听到了吗')

res = yaml.load(f)
logger.info('成功加载配置文件')
f.close()


# 从config.yaml获取环境变量
def value(v):
    return res[v]
