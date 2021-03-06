#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-27 18:24:04
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import time
import logging


def Logs():

    try:
        t = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
        # 当前目录
        curPath = os.path.abspath(os.path.dirname(__file__))
        # 项目根目录
        rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
        if os.path.exists(rootPath+"Logs") is False:
            os.makedirs(rootPath+"Logs")
        # print(rootPath)
        url_log = rootPath + 'Logs/run_log.log' 
        # url_log = os.path.abspath(os.path.dirname(os.getcwd())) + '/logs/run_result_%s.log' %t
        # url_log = "D:/Python_Demo/NewType/Eddid_CRM/Logs/run_result.log"
        # 获取logger对象，设置日志级别
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)

        # 获取文件处理器，并设置级别
        handler = logging.FileHandler(filename=url_log, encoding='utf-8')
    except Exception as e:
        url_log = os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))) + '/logs/run_result.log' 
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
    lg = Logs()
    lg.info("1111")
