#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo
from bson.objectid import ObjectId
import Logging

class Database:
	log = Logging.logs()

	link_data = []
	collections = set()
	table = {
		'applyId' : 'apply' ,
		'accountId' : 'account',
		'applyInfoIds' : 'apply_info',
		'clientId' : 'client_info',
		'idpUserId' : 'users'
	}

	def __init__(self, host, database):
		self.log.info("连接数据库%s" %database)
		self.client = pymongo.MongoClient(host)
		self.db = self.client[database]
		self.database = database

	def __del__(self):
		self.log.info("close Client")
		self.client.close()


	def del_linked(self, collection, query, database=None):
		# if database == None:
		# 	self.db = self.client[self.database]
		# else:
		# 	self.db = self.client[database]

		self.collections.add(collection)
		result = self.db[collection].find(query)
		self.log.info("%s 表符合查询条件%s 的数据有%s 条" %(collection, query, result.count()))
		print("%s 表符合查询条件%s 的数据有%s 条" %(collection, query, result.count()))
		for r in result:
			# print(r)
			self.log.info(r)
			# continue
			index = 0	#用于记录查询数据的字段个数
			for key in r.keys():
				index += 1
				if key != '_id':
					# 判断是否在表中有ObjectID
					if isinstance(r[key], ObjectId):
						try:
							if self.table[key] not in self.collections:
								self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
								self.log.info("正在查询关联表 %s 的数据" %self.table[key])

								print(collection,"表关联的字段为 ",key,":",r[key])
								print("正在查询关联表 %s 的数据" %self.table[key])

								self.del_linked(self.table[key], {'_id':r[key]})

						except Exception as e:
							self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)
							print(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

					elif isinstance(r[key], list):

						for n in range(len(r[key])):
							# 判断数组中的字段是否是object类型
							if isinstance(r[key][n], ObjectId):
								# continue
								try:
									if self.table[key] not in self.collections:
										self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
										self.log.info("正在查询关联表 %s 的数据" %self.table[key])

										print(collection,"表关联的字段为 ",key,":",r[key][n])
										print("正在查询关联表 %s 的数据" %self.table[key])

										self.del_linked(self.table[key], {'_id':r[key][n]})

								except Exception as e:
									self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)
									print(e," table[%s]没有与之对应的数据库表" %key)

					elif key == 'idpUserId':
						continue
						try:
							if self.table[key] not in self.collections:
								self.log.info("%s 表关联的字段为 %s : %s" %(collection,key,r[key]))
								self.log.info("正在查询关联表 %s 的数据" %self.table[key])

								print(collection,"表关联的字段为 ",key,":",r[key])
								print("正在查询关联表 %s 的数据" %self.table[key])

								self.del_linked(self.table[key], {'subject':r[key]}, database='eddidclientpool%s' %self.database)

						except Exception as e:
							self.log.info(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)
							print(e," table[%s]没有与之对应的数据库表,请查看字段所关联的表table" %key)

					else:
						# print("index", index)
						if index >= len(r) :
							self.log.info("***********************************\n")
							self.log.info('没有关联数据,直接删除%s 表' %collection)
							print('没有关联数据,直接删除%s 表' %collection)

							# result = self.db[collection].remove(query)
							# self.log.info(result)
							# print(result)

							self.log.info("***********************************\n")

if __name__ == '__main__':
	host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
	# host = 'localhost:27017'
	database = 'uat'
	# Database(host, database).del_linked("apply_info", {'email':'onedi@qq.com'})
	Database(host, database).del_linked("client_info", {'email':"540onedi2s5168@qq.com"})









