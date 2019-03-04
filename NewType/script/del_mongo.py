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
		print("%s ����ϲ�ѯ����%s ��������%s ��" %(collection, query, result.count()))
		for r in result:
			print(r)
			# continue
			index = 0	#���ڼ�¼��ѯ���ݵ��ֶθ���
			for key in r.keys():
				index += 1
				if key != '_id':
					# �ж��Ƿ��ڱ�����ObjectID
					if isinstance(r[key], ObjectId):
						try:
							if self.table[key] not in self.collections:
								print(collection,"��������ֶ�Ϊ ",key,":",r[key])
								print("���ڲ�ѯ������ %s ������" %self.table[key])
								self.del_linked(self.table[key], {'_id':r[key]})

						except Exception as e:
							print(e," table[%s]û����֮��Ӧ�����ݿ��,��鿴�ֶ��������ı�table" %key)

					elif isinstance(r[key], list):

						for n in range(len(r[key])):
							# �ж������е��ֶ��Ƿ���object����
							if isinstance(r[key][n], ObjectId):
								# continue
								try:
									if self.table[key] not in self.collections:
										print(collection,"��������ֶ�Ϊ ",key,":",r[key][n])
										print("���ڲ�ѯ������ %s ������" %self.table[key])
										self.del_linked(self.table[key], {'_id':r[key][n]})

								except Exception as e:
									print(e," table[%s]û����֮��Ӧ�����ݿ��" %key)

					else:
						# print("index", index)
						if index >= len(r) :
							print('û�й�������,ֱ��ɾ��%s ��' %collection)
							result = self.db[collection].remove(query)
							print(result)

if __name__ == '__main__':
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	Database('test7').del_linked("client_info", {'idNumber':"4311211838"})









