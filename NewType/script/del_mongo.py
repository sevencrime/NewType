#!/usr/bin/env python
# -*- coding: GBK -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo
from bson.objectid import ObjectId

class Database:

	table = {
		'semester' : 'product' ,
		'semesster' : 'product'
	}

	def __init__(self):
		self.client = pymongo.MongoClient("mongodb://localhost:27017/")
		self.db = self.client.test

	def __del__(self):
		self.client.close()


	def del_linked(self, collection, query):
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
						print(collection,"表关联的字段为 ",key,":",r[key])
						try:
							print("正在查询关联表 %s 的数据" %self.table[key])
							res_two = self.del_linked(self.table[key], {'abc':r[key]})
							# print("ssssssssssss",res_two)
							print("查询完毕,删除")

						except Exception as e:
							print(e," table[%s]没有与之对应的数据库表" %key)
					else:
						print("index", index)
						if index >= len(r) :
							print('没有关联数据,直接删除')
						# result = self.db[collection].remove()
						# print(result)
		return result

if __name__ == '__main__':
	Database().del_linked("orders", None)









