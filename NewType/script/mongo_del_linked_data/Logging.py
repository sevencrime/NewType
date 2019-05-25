#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 14:16:58
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import time
import logging


def logs():

    t = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
    if os.path.exists(os.getcwd()+'/logs') is False:
        os.makedirs(os.getcwd()+'/logs')
        
    url_log = os.getcwd() + '/logs/%s_run_result.log' % t

    # url_log = os.getcwd()+'/logs/run_result.log'
    # 获取logger对象，设置日志级别
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)

    # 获取文件处理器，并设置级别
    handler = logging.FileHandler(filename=url_log, encoding='utf-8')
    # handler = logging.FileHandler("./logs/log.csv")
    handler.setLevel(logging.INFO)

    # 获取并设置文件处理器的日志格式
    formatter = logging.Formatter(
        '%(asctime)s %(filename)s %(levelname)s [line:%(lineno)d] %(message)s')
    handler.setFormatter(formatter)

    # 设置日志处理器
    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    lg = logs()
    lg.info("1111")
