#!/usr/bin/env python
# -*- coding: GBK -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo
from bson.objectid import ObjectId

class Database:

	collections = set()
	table = {
		'applyId' : 'apply' ,
		'accountId' : 'account',
		'applyInfoIds' : 'apply_info',
		'clientId' : 'client_info'
	}

	def __init__(self, database):
		self.client = pymongo.MongoClient("mongodb://localhost:27017/")
		self.db = self.client[database]

	def __del__(self):
		self.client.close()


	def del_linked(self, collection, query):
		self.collections.add(collection)
		result = self.db[collection].find(query)
		print("%s 表符合查询条件%s 的数据有%s 条" %(collection, query, result.count()))
		for r in result:
			print(r)
			# continue
			index = 0	#用于记录查询数据的字段个数
			for key in r.keys():
				index += 1
				if key != '_id':
					# 判断是否在表中有ObjectID
					if isinstance(r[key], ObjectId):
						try:
							if self.table[key] not in self.collections:
								print(collection,"表关联的字段为 ",key,":",r[key])
								print("正在查询关联表 %s 的数据" %self.table[key])
								self.del_linked(self.table[key], {'_id':r[key]})

						except Exception as e:
							print(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

					elif isinstance(r[key], list):

						for n in range(len(r[key])):
							# 判断数组中的字段是否是object类型
							if isinstance(r[key][n], ObjectId):
								# continue
								try:
									if self.table[key] not in self.collections:
										print(collection,"表关联的字段为 ",key,":",r[key][n])
										print("正在查询关联表 %s 的数据" %self.table[key])
										self.del_linked(self.table[key], {'_id':r[key][n]})

								except Exception as e:
									print(e," table[%s]没有与之对应的数据库表" %key)

					else:
						# print("index", index)
						if index >= len(r) :
							print('没有关联数据,直接删除%s 表' %collection)
							result = self.db[collection].remove(query)
							print(result)

if __name__ == '__main__':
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	Database('test7').del_linked("client_info", {'idNumber':"4311211838"})









