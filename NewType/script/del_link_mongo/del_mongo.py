#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo
import argparse

def del_link_mongo_new(phone, collection=None, env="uat", remove=True):

    if phone == "" or phone == None:
        print("手机号不能为空")
        return True

    tables = {}
    _users = set()
    _usersdriver = set()
    _apply = set()
    _apply_info = set()
    _client_info = set()
    _account = set()
    _aosUsers = set()

    host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
    aoshost = 'mongodb://aos-v2-user:8y1PKcJRWDzcqzSJ@dds-wz9fb08463a61eb41356-pub.mongodb.rds.aliyuncs.com:3717,dds-wz9fb08463a61eb42750-pub.mongodb.rds.aliyuncs.com:3717/aos-v2-{env}?authSource=aos-v2-{env}&replicaSet=mgset-15579011'.format(env=env)
    client = pymongo.MongoClient(host)
    aosClient = pymongo.MongoClient(aoshost)


    if env == "test":
        idp = "eddidclientpool"
        crm = "test"
        aos = "aos-v2-test"
    elif env == "uat":
        idp = "eddidclientpooluat"
        crm = "uat"
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
            print("idp为 : {}".format(applyd['idpUserId']))
            _apply.add(applyd['_id'])
            _apply_info = _apply_info | set(applyd['applyInfoIds'])
            # 查询account表
            # for acc in client[crm]["account"].find({"idpUserId": applyd['idpUserId']}):
            #     _account.add(acc["_id"])
            #     import pdb; pdb.set_trace()
            #     _client_info = _client_info | set(acc['clientId'])

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

    if remove:
        print("开始执行删除操作: \n")

        if collection:
            for _id in tables[collection]:
                if collection == "users" or collection == "usersdriver":
                    result = client[idp][collection].delete_one({"_id" : _id})
                    print("{} 表删除数据 : {}".format(collection, _id))
                elif collection == "aosUsers" :
                    result = aosClient[aos]['users'].delete_one({"_id" : _id})
                    print("{} 表删除数据 : {}".format(collection, _id))
                else:
                    result = client[crm][collection].delete_one({"_id" : _id})
                    print("{} 表删除数据 : {}".format(collection, _id))

            return True


        for _key, _value in tables.items():
            for _id in _value:
                if _key == "users" or _key == "usersdriver":
                    result = client[idp][_key].delete_one({"_id" : _id})
                    print("{} 表删除数据 : {}".format(_key, _id))
                elif _key == "aosUsers" or _key == "aosusers":
                    result = aosClient[aos]['users'].delete_one({"_id" : _id})
                    print("{} 表删除数据 : {}".format(_key, _id))
                else:
                    result = client[crm][_key].delete_one({"_id" : _id})
                    print("{} 表删除数据 : {}".format(_key, _id))


    client.close()
    aosClient.close()


parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--phone', '-p', help='phone 属性，必要参数, 查询的电话号码')
parser.add_argument('--collection', '-c', help='collection 属性，非必要参数，删除单个表的表名, 有默认值', default=None)
parser.add_argument('--env', '-e', help='env 属性，非必要参数, 查询的环境, 有默认值', default="uat")
parser.add_argument('--remove', '-r', help='remove 属性，非必要参数, 决定是否需要删除, 有默认值', default=True)
args = parser.parse_args()


if __name__ == '__main__':
    # del_link_mongo_new("13528802757")
    try:
        del_link_mongo_new(args.phone, args.collection, args.env, (False if args.remove == 'False' or args.remove == 'false' else True))
    except Exception as e:
        print(e)
