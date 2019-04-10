#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-21 10:10:26
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
import pymongo
from Commons import Modify_xls

class Pymongo:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
        # db = client.uat
        # self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['uat']

    def __del__(self):
        self.client.close()


    def find(self, collection, query):
        result = self.db[collection].find(query)

        if result.count() == 1:
            for res in result:
                return res

        else:
            pass




if __name__ == '__main__':
    r = Pymongo()
    result = r.find('apply', {'applySeqId':1431})
    print(result)
