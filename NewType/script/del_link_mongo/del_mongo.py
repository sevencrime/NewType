#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo
from pymongo.collection import ReturnDocument
import argparse
import ast
import time
import json
from bson import json_util
from bson.objectid import ObjectId
import datetime


def to_json(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), cls=JSONEncoder, ensure_ascii=False)

class JSONEncoder(json.JSONEncoder):
    """处理ObjectId & datetime类型无法转为json"""
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return datetime.datetime.strftime(o, '%Y-%m-%d %H:%M:%S')

        return json.JSONEncoder.default(self, o)


def del_link_mongo_new(phone, collections=None, finddata=False, env="uat", update=None):

    # 手机号不能为空
    if phone == "" or phone == None:
        print("手机号不能为空")
        return True

    # 存放 各个表的 _id 集合
    tables = {}
    _users = set()
    _usersdriver = set()
    _apply = set()
    _apply_info = set()
    _client_info = set()
    _account = set()
    _aosUsers = set()

    # 连接数据库
    host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net/?authSource=admin&readPreference=primary&replicaSet=dev-clientDB-shard-0&ext.ssl.allowInvalidHostnames=true'
    aoshost = 'mongodb://aos-v2-user:8y1PKcJRWDzcqzSJ@dds-wz9fb08463a61eb41356-pub.mongodb.rds.aliyuncs.com:3717,dds-wz9fb08463a61eb42750-pub.mongodb.rds.aliyuncs.com:3717/aos-v2-{env}?authSource=aos-v2-{env}&replicaSet=mgset-15579011'.format(env=env)
    start1 = time.time()
    client = pymongo.MongoClient(host)
    print("连接host所用的时间为 : ", time.time() - start1)

    start2 = time.time()
    aosClient = pymongo.MongoClient(aoshost)
    print("连接aos_host所用的时间为 : ", time.time() - start2)


    if env == "test":
        idp = "eddidclientpool"
        crm = "test"
        aos = "aos-v2-test"
    elif env == "uat":
        idp = "eddidclientpooluat"
        crm = "uat"
        aos = "aos-v2-uat"

    idptime = time.time()
    # 查询idpusers表和uuids表
    for idpUser in client[idp]['users'].find({"phone_number":{"$regex":".+{}".format(phone)}}):
    # for idpUser in client[idp]['users'].find({"phone_number" : "86{}".format(phone)}):
        print("idp为 : {}".format(idpUser['subject']))
        _users.add(idpUser['_id'])
        # print("第一个点 ", time.time() - idptime)
        for usersdriver in client[idp]['userdevices'].find({"subject" : idpUser['subject']}):
            _usersdriver.add(usersdriver['_id'])

        # print("第二个点 ", time.time() - idptime)
        for applyId in client[crm]['apply'].find({"idpUserId": idpUser['subject']}):
            _apply.add(applyId["_id"])

        # print("第三个点 ", time.time() - idptime)

    print("查询idp所用的时间的为 : ", time.time() - idptime)

    applytime = time.time()
    # 查询apply_info和apply表
    for applyinfos in client[crm]['apply_info'].find({"phone":phone}):
        _apply_info.add(applyinfos['_id'])
        # 查询apply表
        for applyd in client[crm]['apply'].find({'_id':applyinfos['applyId']}):
            print("idp为 : {}".format(applyd['idpUserId']))
            _apply.add(applyd['_id'])
            _apply_info = _apply_info | set(applyd['applyInfoIds'])
    print("查询apply所用的时间为 : ", time.time() - applytime)

    clienttime = time.time()
    # 查询client_info表和account表
    for clientinfos in client[crm]["client_info"].find({"phone":phone}):
        _client_info.add(clientinfos["_id"])
        for accountid in clientinfos['accountId']:
            for acc in client[crm]["account"].find({'_id':accountid}):
                _account.add(acc["_id"])

    print("查询client所用的时间为 : ", time.time() - clienttime)

    aostime = time.time()
    for aosdata in aosClient[aos]['users'].find({"phone" : phone}):
        # print("aos表的数据为 : {} \n", aosdata)
        _aosUsers.add(aosdata['_id'])
    print("查询aos所用的时间为 : ", time.time() - aostime)


    tables['users'] = list(_users)
    tables['userdevices'] = list(_usersdriver)
    tables['apply'] = list(_apply)
    tables['apply_info'] = list(_apply_info)
    tables['client_info'] = list(_client_info)
    tables['account'] = list(_account)
    tables['aosUsers'] = list(_aosUsers)

    # print("\n查询的所有数据的_id为 : \n", tables)
    print("\n查询的所有数据的_id为 : \n", to_json(tables))


    if collections:
        for collection in collections:
            for _id in tables[collection]:
                if collection == "users" or collection == "userdevices":
                    if update:
                        result = client[idp][collection].find_one_and_update({"_id" : _id}, update[collection], return_document=ReturnDocument.AFTER)
                        print("\n {} 表修改后的数据为 : {}".format(collection, result))
                        continue

                    result = client[idp][collection].remove({"_id" : _id})
                    print("{} 表删除数据 : {}".format(collection, _id))
                elif collection == "aosUsers" :
                    if update:
                        result = aosClient[aos]['users'].find_one_and_update({"_id" : _id}, update[collection], return_document=ReturnDocument.AFTER)
                        print("\n {} 表修改后的数据为 : {}".format(collection, result))
                        continue

                    result = aosClient[aos]['users'].remove({"_id" : _id})
                    print("{} 表删除数据 : {}".format(collection, _id))
                else:
                    if update:
                        result = client[crm][collection].find_one_and_update({"_id" : _id}, update[collection], return_document=ReturnDocument.AFTER)
                        print("\n {} 表修改后的数据为 : {}".format(collection, result))
                        continue
                    result = client[crm][collection].remove({"_id" : _id})
                    print("{} 表删除数据 : {}".format(collection, _id))

        return True


    for _key, _value in tables.items():
        for _id in _value:
            if _key == "users" or _key == "userdevices":
                if finddata:
                    for _d in client[idp][_key].find({"_id" : _id}):
                        print("\n {} 表的数据为 \n: {}".format(_key, to_json(_d)))
                    continue

                result = client[idp][_key].remove({"_id" : _id})
                print("{} 表删除数据 : {}".format(_key, _id))
            elif _key == "aosUsers" or _key == "aosusers":
                if finddata:
                    for _d in aosClient[aos]['users'].find({"_id" : _id}):
                        print("\n {} 表的数据为 \n: {}".format(_key, to_json(_d)))
                    continue

                result = aosClient[aos]['users'].remove({"_id" : _id})
                print("{} 表删除数据 : {}".format(_key, _id))
            else:
                if finddata:
                    for _d in client[crm][_key].find({"_id" : _id}):
                        print("\n {} 表的数据为 \n: {}".format(_key, to_json(_d)))
                    continue

                result = client[crm][_key].remove({"_id" : _id})
                print("{} 表删除数据 : {}".format(_key, _id))


    client.close()
    aosClient.close()


parser = argparse.ArgumentParser(description='删除mongo关联表, 需指定phone参数, H5的表为: aosUsers, idp表的名字为users')
parser.add_argument('--phone', '-p', help='phone 属性，必要参数, 查询的电话号码')
parser.add_argument('--collections', '-c', help='collection 属性，list类型, 非必要参数，删除单个表的表名, 默认值为False, eg: {}'.format("['collection']"), default=None, type=ast.literal_eval)
parser.add_argument('--finddata', '-f', help='finddata 属性，非必要参数，是否只查询数据而不删除, -f 默认为True', action="store_true")
parser.add_argument('--env', '-e', help='env 属性，非必要参数, 查询的环境, 有默认值=uat', default="uat")
parser.add_argument('--update', '-u', help='update 属性，dict类型, 非必要参数, 修改数据, 需和-c一起使用, 有默认值', default=None, type=ast.literal_eval)
args = parser.parse_args()


if __name__ == '__main__':
    # del_link_mongo_new("13528802757")
    try:
        # del_link_mongo_new(args.phone, args.collection, args.finddata, args.env, (False if args.remove == 'False' or args.remove == 'false' else True))
        del_link_mongo_new(args.phone, args.collections, args.finddata, args.env, args.update)
    except Exception as e:
        print(e)


'''
注册后, 修改users和aosUser的phone 和 email
python del_mongo.py -c "['users', 'aosUsers']" -u "{ 'users': {'$set' : {'phone_number' : '8615033331111', 'preferred_username' : '15033331111', 'email' : '15033331111@123.com'} }, 'aosUsers' : {'$set' : {'phone' : '15033331111', 'email' : '15033331111@123.com'} } }" - p 15089514626

开通交易账号后, 修改phone, email, idNumber
python del_mongo.py -c "['users', 'aosUsers', 'apply_info', 'client_info']" -u "{ 'users': {'$set' : {'phone_number' : '8615033331111', 'preferred_username' : '15033331111', 'email' : '15033331111@123.com'} }, 'aosUsers' : {'$set' : {'phone' : '15033331111', 'email' : '15033331111@123.com', 'idNumber' : '441502199502112334'} }, 'apply_info' : {'$set' : {'phone' : '15033331111', 'email' : '15033331111@123.com', 'idNumber' : '441502199502112334'} }, 'client_info' : {'$set' : {'phone' : '15033331111', 'email' : '15033331111@123.com', 'idNumber' : '441502199502112334'} }  }" -p 15089514626
'''