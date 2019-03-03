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
						print(collection,"��������ֶ�Ϊ ",key,":",r[key])
						try:
							print("���ڲ�ѯ������ %s ������" %self.table[key])
							res_two = self.del_linked(self.table[key], {'abc':r[key]})
							# print("ssssssssssss",res_two)
							print("��ѯ���,ɾ��")

						except Exception as e:
							print(e," table[%s]û����֮��Ӧ�����ݿ��" %key)
					else:
						print("index", index)
						if index >= len(r) :
							print('û�й�������,ֱ��ɾ��')
						# result = self.db[collection].remove()
						# print(result)
		return result

if __name__ == '__main__':
	Database().del_linked("orders", None)









