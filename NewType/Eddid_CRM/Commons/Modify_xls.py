#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-19 17:41:50
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


import xlrd 
import os

class Modifyxls():

    def readxls(self,file_url):

        path = os.path.abspath(os.path.dirname(os.getcwd()))+file_url
        # print(path)
        # 打开excel文件,open_workbook(path),path为excel所在的路径
        workbook = xlrd.open_workbook(path)
        # 打开excel表,这里表示打开第一张表
        table = workbook.sheets()[0]

        nrows = table.nrows     # 获取excel的行数
        # print(nrows)
        ncols = table.ncols     #获取excel的列数
        # print(ncols)
        keys = table.row_values(0)      #获取第一行的值
        # print(keys)

        Data = []       #创建一个list，用于存放
        x = 1
        for i in range(nrows-1):
            s = {}
            # print(i)
            values = table.row_values(x)
            # print(values)
            for j in range(ncols):
                # print('j=',j)
                s[keys[j]] = values[j]
            # print(s)
            Data.append(s)
            x += 1

        return Data


if __name__ == "__main__":

    modify = Modifyxls()
    file_url = '/config/Ayers1.xls'
    data = modify.readxls(file_url)
    print(data)