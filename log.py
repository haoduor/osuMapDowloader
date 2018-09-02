# -*- encoding:utf-8 -*-

import logging
import time
from logging.handlers import TimedRotatingFileHandler

formattStr = '[%(asctime)s]-%(levelname)s-[%(filename)s:%(funcName)s:%(lineno)d]:%(message)s'
formatter = logging.Formatter(formattStr)

logging.basicConfig(level=logging.NOTSET,
                    format=formattStr)
logger = logging.getLogger('gu')

timeStr = time.strftime("%Y%m%d", time.localtime(time.time()))
logName = 'log_%s.log' % timeStr

fileHandler = TimedRotatingFileHandler(filename=logName,
                                       when='D',
                                       interval=1,
                                       backupCount=20)
fileHandler.setLevel(logging.NOTSET)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)


def getlogger():
    return logger
