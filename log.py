import logging

logging.basicConfig(level=logging.NOTSET, format='[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger('gu')
logger.info('i am in')
