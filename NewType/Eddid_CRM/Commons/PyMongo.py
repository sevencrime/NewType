#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-21 10:10:26
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
import pymongo
from bson.objectid import ObjectId
from collections import Counter
from Commons import Logging

class Database:
    
    log = Logging.Logs()
    collectionsId = set()       #存放已经遍历过的数据库表的id
    expectedRemoveTotal = []        #预期删除总数
    actualRemoveTotal = []      #实际删除总数
    table = {
        'applyId' : 'apply' ,
        'accountId' : 'account',
        'applyInfoIds' : 'apply_info',
        'clientId' : 'client_info',
        'idpUserId' : 'users' , 
        'subject' : 'userdevices',
        'leadId' : 'lead'
    }


    def __init__(self, database="uat"):
        host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
        self.log.info("连接数据库%s" %database)
        self.client = pymongo.MongoClient(host)     #连接数据库
        self.db = self.client[database]     #指定数据库
        self.database = database    #用于切换数据库返回

    def __del__(self):
        self.log.info("close Client")
        self.client.close()     #关闭数据库

        expectedTotal = set(self.expectedRemoveTotal)
        for item in expectedTotal:  #输出删除总数
            self.log.info("%s 表预计删除 %d 条记录" %(item, self.expectedRemoveTotal.count(item)))

        actualTotal = set(self.actualRemoveTotal)
        for actual in actualTotal:
            self.log.info("%s 表实际删除 %d 条记录" %(actual, self.actualRemoveTotal.count(actual)))


    """
        collection : 查询的数据库表
        query : 查询条件
        database : 查询的数据库
    """
    def del_linked(self, collection, query, database=None):
        collections = set()  #存放关联记录中遍历过的表
        if database != None:
            # 如果database不等于None则切换数据库
            self.db = self.client[database]

        result = self.db[collection].find(query)
        self.log.info("%s 表符合查询条件%s 的数据有%s 条" %(collection, query, result.count()))
        for r in result:
            self.log.info(r)
            collections.add(collection)

            if str(r['_id']) in self.collectionsId:
                continue
            self.collectionsId.add(str(r['_id']))
            index = 0   #用于记录查询数据的字段个数
            for key in r.keys():
                index += 1
                if key != '_id':
                    # 判断是否在表中有ObjectID
                    if isinstance(r[key], ObjectId):
                        try:
                            if r[key] not in self.collectionsId and self.table[key] not in collections:
                                self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
                                self.log.info("正在查询关联表 %s 的数据" %self.table[key])


                                self.del_linked(self.table[key], {'_id':r[key]})

                        except Exception as e:
                            self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

                    elif isinstance(r[key], list):

                        for n in range(len(r[key])):
                            # 判断数组中的字段是否是object类型
                            if isinstance(r[key][n], ObjectId):
                                try:
                                    if r[key][n] not in self.collectionsId and self.table[key] not in collections:
                                        self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
                                        self.log.info("正在查询关联表 %s 的数据" %self.table[key])


                                        self.del_linked(self.table[key], {'_id':r[key][n]})

                                except Exception as e:
                                    self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

                    elif key == 'idpUserId':
                        # continue
                        try:
                            if r[key] not in self.collectionsId and self.table[key] not in collections:
                                self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
                                self.log.info("正在查询关联表 %s 的数据" %self.table[key])

                                self.del_linked(self.table[key], {'subject':r[key]}, database='eddidclientpool{database}'.format(database=self.database))


                        except Exception as e:
                            self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

                    elif key == 'subject':
                        # continue
                        try:
                            if r[key] not in self.collectionsId and self.table[key] not in collections :
                                self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
                                self.log.info("正在查询关联表 %s 的数据" %self.table[key])


                                self.del_linked(self.table[key], {'subject':r[key]}, database='eddidclientpool{database}'.format(database=self.database))


                        except Exception as e:
                            self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

                    else:
                        if index >= len(r) :
                            self.log.info("***********************************\n")
                            self.log.info('没有关联数据,直接删除%s 表' %collection)
                            self.expectedRemoveTotal.append(collection)     #添加所有需要删除的表,统计总数

                            if database == None:
                                self.db = self.client[self.database]

                            # 删除操作,请先查询后,确定数据以后再执行删除操作
                            result = self.db[collection].delete_one(query)
                            if result.deleted_count > 0 :
                              self.actualRemoveTotal.append(collection)
                            
                            self.log.info(result)


                            self.log.info("***********************************\n")


if __name__ == '__main__':
    host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
    # host = 'localhost:27017'
    database = 'uat'    #查询的数据库
    Database(host, database).del_linked("client_info", {"email":"15089514626@sina.cn"}) # 传入需要查询的表和查询条件

    # Database(host, database).del_linked("apply_info", {'email':{"$regex" : ".*onedi.*"}})
    
