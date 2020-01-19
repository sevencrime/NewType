#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo

def del_link_mongo_new(self, phone, env="uat", collection=None):

    # 传入phone
    # 查询idpusers, 获取idp

    tables = {}
    _users = set()
    _usersdriver = set()
    _apply = set()
    _apply_info = set()
    _client_info = set()
    _account = set()
    _aosUsers = set()

    host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
    client = pymongo.MongoClient(host)

    if env == "test":
        idp = "eddidclientpool"
        crm = "test"
        aoshost_test = 'mongodb://aos-v2-user:8y1PKcJRWDzcqzSJ@dds-wz9fb08463a61eb41356-pub.mongodb.rds.aliyuncs.com:3717,dds-wz9fb08463a61eb42750-pub.mongodb.rds.aliyuncs.com:3717/aos-v2-test?authSource=aos-v2-test&replicaSet=mgset-15579011'
        aosClient = pymongo.MongoClient(aoshost_test)
        aos = "aos-v2-test"
    elif env == "uat":
        idp = "eddidclientpooluat"
        crm = "uat"
        aoshost_uat = 'mongodb://aos-v2-user:8y1PKcJRWDzcqzSJ@dds-wz9fb08463a61eb41356-pub.mongodb.rds.aliyuncs.com:3717,dds-wz9fb08463a61eb42750-pub.mongodb.rds.aliyuncs.com:3717/aos-v2-uat?authSource=aos-v2-uat&replicaSet=mgset-15579011'
        aosClient = pymongo.MongoClient(aoshost_uat)
        aos = "aos-v2-uat"

    # 查询idpusers表和uuids表
    for idpUser in client[idp]['users'].find({"phone_number":{"$regex":".+{}".format(phone)}}):
        print("idp为 : {}".format(idpUser['subject']))
        _users.add(idpUser['_id'])
        for usersdriver in client[idp]['userdevices'].find({"subject" : idpUser['subject']}):
            _usersdriver.add(usersdriver['_id'])

        for applyId in client[crm]['apply'].find({"idpUserId": idpUser['subject']}):
            _apply.add(applyId["_id"])

    # 查询apply_info和apply表
    for applyinfos in client[crm]['apply_info'].find({"phone":phone}):
        _apply_info.add(applyinfos['_id'])
        # 查询apply表
        for applyd in client[crm]['apply'].find({'_id':applyinfos['applyId']}):
            _apply.add(applyd['_id'])
            _apply_info = _apply_info | set(applyd['applyInfoIds'])
            # 查询account表
            for acc in client[crm]["account"].find({"idpUserId": applyd['idpUserId']}):
                _account.add(acc["_id"])
                _client_info = _client_info | set(acc['clientId'])

    # 查询client_info表和account表
    for clientinfos in client[crm]["client_info"].find({"phone":phone}):
        _client_info.add(clientinfos["_id"])
        for accountid in clientinfos['accountId']:
            for acc in client[crm]["account"].find({'_id':accountid}):
                _account.add(acc["_id"])

    for aosdata in aosClient[aos]['users'].find({"phone" : phone}):
        _aosUsers.add(aosdata['_id'])


    tables['users'] = _users
    tables['usersdriver'] = _usersdriver
    tables['apply'] = _apply
    tables['apply_info'] = _apply_info
    tables['client_info'] = _client_info
    tables['account'] = _account
    tables['aosUsers'] = _aosUsers

    print("查询的数据为 : \n", tables)

    print("开始执行删除操作: \n")

    if collection:
        for _id in tables[collection]:
            if collection == "users" or collection == "usersdriver":
                result = client[idp][collection].delete_one({"_id" : _id})
            elif _key == "aosUsers" :
                result = aosClient[aos]['users'].delete_one({"_id" : _id})
            else:
                result = client[crm][_key].delete_one({"_id" : _id})


    for _key, _value in tables.items():
        for _id in _value:
            if _key == "users" or _key == "usersdriver":
                result = client[idp][_key].delete_one({"_id" : _id})
                print("{} 表删除数据 : {}".format(_key, _id))
            elif _key == "aosUsers" :
                result = aosClient[aos]['users'].delete_one({"_id" : _id})
                print("{} 表删除数据 : {}".format(_key, _id))
            else:
                result = client[crm][_key].delete_one({"_id" : _id})
                print("{} 表删除数据 : {}".format(_key, _id))


    client.close()
    aosClient.close()


if __name__ == '__main__':
    # host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net/?authSource=admin'
    # aosUAThost="mongodb://aos-v2-user:8y1PKcJRWDzcqzSJ@dds-wz9fb08463a61eb41356-pub.mongodb.rds.aliyuncs.com:3717,dds-wz9fb08463a61eb42750-pub.mongodb.rds.aliyuncs.com:3717/aos-v2-uat?authSource=aos-v2-uat&replicaSet=mgset-15579011"

    del_link_mongo_new("13528802757")
