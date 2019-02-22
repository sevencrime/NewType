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

class Pymongo():

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
            return self.collection.find({'idNumber': self.data['id_code'], 'email': self.data['email']})

        else:
            print("查询数据库数据为空")
            id_code = Modify_xls.Modifyxls().writexls()
            Client(id_code)
            # 失败,或者修改id_code


if __name__ == '__main__':
    file_url = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xls'
    data = Modify_xls.Modifyxls(file_url).readxls()

    Pymongo('uat','client_info', data).Client()

