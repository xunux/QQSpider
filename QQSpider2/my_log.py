#!/usr/bin/env python
# --coding: utf-8 --


import os
import logging
import config
from logging.handlers import TimedRotatingFileHandler


def getLogger(log_name=None, logger=None):
    if not os.path.exists(config.log_path):
        os.mkdir(config.log_path)

    # logging.basicConfig(level = logging.INFO)
    #logging.getLogger().handlers = []   # 删除所有的handler

    if logger:
        log = logging.getLogger(logger)
    else:
        log = logging.getLogger("mylogger")
        
    if not log_name:
        log_name = config.log_name
    log.setLevel(logging.INFO)

    #formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s][line:%(lineno)d]: %(message)s')
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s]: %(message)s')

    # 文件日志 appender
    fileTimeHandler = TimedRotatingFileHandler(config.log_path + log_name, "D", 1, 10)
    fileTimeHandler.suffix = "%Y%m%d"
    fileTimeHandler.setFormatter(formatter)
    fileTimeHandler.setLevel(logging.INFO)

    # console控制台日志 appender
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    # 将定义好的console日志handler添加到 mylogger
    
    log.handlers = []
    log.addHandler(fileTimeHandler)
    log.addHandler(console)

    return log
