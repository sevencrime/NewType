#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-21 10:10:26
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
import pymongo
from Commons import Modify_xls

class Pymongo:

    def __init__(self, database, table, data):
        client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
        # db = client['uat']
        # self.collection = db['client_info']
        db = client[database]
        self.collection = db[table]        
        self.data = data

    def Client(self):

        # result_sum = collection.find({'idNumber': "3705342352375412"}).count()
        result = self.collection.find({'idNumber': self.data['id_code'], 'email': self.data['email']})

        if result != None:
            for res in result:
                return res

        else:
            print("查询数据库数据为空")
            id_code = Modify_xls.Modifyxls().writexls()
            Client(id_code)
            # 失败,或者修改id_code


if __name__ == '__main__':
    file_url = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xlsx'
    data = Modify_xls.Modifyxls(file_url).readxls()
    if len(data) == 1:
        for d in data:
            #导入数据库前先查询数据库,保证数据库没有该记录
            # PyMongo.Pymongo('uat', 'client_info').Client(data['id_code'])
            res = Pymongo('uat', 'client_info', d).Client()
            print(res)
            print(type(res))

