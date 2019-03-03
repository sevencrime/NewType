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

    def __init__(self, collection):
        # client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
        # db = client.uat
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client.test
        self.collection = db.orders       

    def find(self, options):
        # result_sum = collection.find({'idNumber': "3705342352375412"}).count()
        # result = self.collection.find({'idNumber': self.data['id_code'], 'email': self.data['email']})
        return self.collection.find(options)

    def delete(self, options):

        result = self.collection.remove(options)
        print(result)

    def insert(self, options):
        # 返回_id
        return self.collection.insert(options)

if __name__ == '__main__':
    r = Pymongo('orders').find({})
    print(r)


    # file_url = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xlsx'
    # data = Modify_xls.Modifyxls(file_url).readxls()

    # # res = Pymongo().Find({'idNumber': data[0]['id_code'], 'email': data[0]['email']})
    # res = Pymongo().Find({'idNumber': '8623253145165'})
    # print(res)
    # a = [r for r in res]
    # print(a)
    # print(a[0])
    # print(a[0]['title'])