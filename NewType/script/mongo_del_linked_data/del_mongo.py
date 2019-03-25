#!/usr/bin/env python
# -*- coding: GBK -*-
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
		'clientId' : 'client_info'
	}

	def __init__(self, host, database):
		self.log.info("�������ݿ�%s" %database)
		self.client = pymongo.MongoClient(host)
		self.db = self.client[database]

	def __del__(self):
		self.log.info("close Client")
		self.client.close()


	def del_linked(self, collection, query):
		self.collections.add(collection)
		result = self.db[collection].find(query)
		self.log.info("%s ����ϲ�ѯ����%s ��������%s ��" %(collection, query, result.count()))
		print("%s ����ϲ�ѯ����%s ��������%s ��" %(collection, query, result.count()))
		for r in result:
			# print(r)
			self.log.info(r)
			# continue
			index = 0	#���ڼ�¼��ѯ���ݵ��ֶθ���
			for key in r.keys():
				index += 1
				if key != '_id':
					# �ж��Ƿ��ڱ�����ObjectID
					if isinstance(r[key], ObjectId):
						try:
							if self.table[key] not in self.collections:
								self.log.info("%s ��������ֶ�Ϊ %s : %s" %(collection,key,r[key]))
								self.log.info("���ڲ�ѯ������ %s ������" %self.table[key])

								print(collection,"��������ֶ�Ϊ ",key,":",r[key])
								print("���ڲ�ѯ������ %s ������" %self.table[key])

								self.del_linked(self.table[key], {'_id':r[key]})

						except Exception as e:
							self.log.info(e," table[%s]û����֮��Ӧ�����ݿ��,��鿴�ֶ��������ı�table" %key)
							print(e," table[%s]û����֮��Ӧ�����ݿ��,��鿴�ֶ��������ı�table" %key)

					elif isinstance(r[key], list):

						for n in range(len(r[key])):
							# �ж������е��ֶ��Ƿ���object����
							if isinstance(r[key][n], ObjectId):
								# continue
								try:
									if self.table[key] not in self.collections:
										self.log.info("%s ��������ֶ�Ϊ %s : %s" %(collection,key,r[key]))
										self.log.info("���ڲ�ѯ������ %s ������" %self.table[key])

										print(collection,"��������ֶ�Ϊ ",key,":",r[key][n])
										print("���ڲ�ѯ������ %s ������" %self.table[key])

										self.del_linked(self.table[key], {'_id':r[key][n]})

								except Exception as e:
									self.log.info(e," table[%s]û����֮��Ӧ�����ݿ��,��鿴�ֶ��������ı�table" %key)
									print(e," table[%s]û����֮��Ӧ�����ݿ��" %key)

					else:
						# print("index", index)
						if index >= len(r) :
							self.log.info("***********************************\n")
							self.log.info('û�й�������,ֱ��ɾ��%s ��' %collection)
							print('û�й�������,ֱ��ɾ��%s ��' %collection)

							# result = self.db[collection].remove(query)
							# self.log.info(result)
							# print(result)

							self.log.info("***********************************\n")

if __name__ == '__main__':
	host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
	# host = 'localhost:27017'
	database = 'uat'
	# Database(host, database).del_linked("apply_info", {'email':'onedi@qq.com'})
	Database(host, database).del_linked("apply_info", {'email':'onedi@qq.com'})









