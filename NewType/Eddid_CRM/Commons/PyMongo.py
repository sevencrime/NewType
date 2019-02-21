#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-21 10:10:26
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import pymongo

class Pymongo():

    def __init__(self, database, table):
        client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
        # db = client['uat']
        # self.collection = db['client_info']
        db = client[database]
        self.collection = db[table]        

    def Client(self, num):
        # result_sum = collection.find({'idNumber': "3705342352375412"}).count()
        result = self.collection.find({'idNumber': num})
        if result != None:
            print(self.collection.find_one({'idNumber': num}))
            return self.collection.find({'idNumber': num})
        else:
            pass
            # 失败,或者修改id_code


if __name__ == '__main__':
    num = '3705342352375412'
    Pymongo('uat','client_info').Client(num)

