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

    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
        db = client['uat']
        self.collection = db['client_info']        

    def Find(self, options):

        # result_sum = collection.find({'idNumber': "3705342352375412"}).count()
        # result = self.collection.find({'idNumber': self.data['id_code'], 'email': self.data['email']})
        result = self.collection.find(options)
        return result





if __name__ == '__main__':
    file_url = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xlsx'
    data = Modify_xls.Modifyxls(file_url).readxls()

    res = Pymongo().Find({'idNumber': data[0]['id_code'], 'email': data[0]['email']})
    # print(res)
    a = [r for r in res]
    print(a)
    print(a[0])
