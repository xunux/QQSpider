# coding=utf-8

import datetime
from init_messages import InitMessages
import spide_controller
import sys

import my_log
log = my_log.getLogger()

reload(sys)
sys.setdefaultencoding("utf-8")  # 设置编码格式

if __name__ == '__main__':
    """ QQSpider的启动文件 """
    try:
        my_messages = InitMessages()  # 读取本地的爬虫信息，并对爬虫进行参数初始化
        spider = spide_controller.SpideController(my_messages=my_messages)
        log.info("%s: Initial work completed! Now, We start:", datetime.datetime.now())
        spider.beginer()  # 开始爬虫
    except Exception, e:
        log.exception("", e)
        log.info(datetime.datetime.now())
    finally:
        log.info('%s: Done! %s ', datetime.datetime.now())
