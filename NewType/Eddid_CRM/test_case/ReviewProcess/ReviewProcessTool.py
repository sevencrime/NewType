#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect

import pytest

from Commons import Logging, GlobalMap, PyMongo
from Interface import apply_create
import unittest
from selenium import webdriver

from PageElement import MainPage, ApplyPage
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class ReviewProcessTool(unittest.TestCase):

	gm = GlobalMap.GlobalMap()
	log = Logging.Logs()

	@pytest.fixture()
	def applyCreateApi(self):
		self.gm.set_value(apiStatus="processing")
		self.gm.set_List("accountType", ["securitiesCash"])
		self.gm.set_value(email = apply_create.apply_create_api())

	@classmethod
	def setUpClass(cls):
		cls.log.info("{cls}类的{func}方法调用apply.create接口创建数据".format(cls=cls.__class__.__name__, func=inspect.stack()[0][3]))
		cls.gm.set_value(email = apply_create.apply_create_api())

	# 所有case执行之后清理环境
	@classmethod
	def tearDownClass(cls):
		cls.log.info("删除数据")
		if cls.gm.get_value("email") != "" or cls.gm.get_value("email") == None:
			PyMongo.Database().del_linked("client_info", {"email": cls.gm.get_value("email")})
			PyMongo.Database().del_linked("apply_info", {"email": cls.gm.get_value("email")})

		cls.log.info("删除变量")
		cls.gm.del_map("email")


	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.set_page_load_timeout(20)
		self.driver.set_script_timeout(20)
		self.url = 'http://eddid-bos-uat.ntdev.be'

		self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

	def tearDown(self):
		self.log.info("结束driver")
		self.driver.quit()


	"""
		# 通过审核
		# 适用于CS1, CS2, RO 状态
		# 通过email,确定需要操作的数据
		# 双击进入apply表单, 点击通过操作

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def reviewPass(self, email, statusSel, *args, **kwarsg):
		publicTool.click_menulist(self, "开户管理", "开户列表")
		publicTool.wait_LoadingModal(self)

		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect(statusSel)
		publicTool.wait_LoadingModal(self)

		# 双击进入apply表单
		self.mainpage.get_apply(email=email)
		publicTool.wait_LoadingModal(self)
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		try:
			if kwarsg['btn_text']:
				self.applypage.click_sublimeApply(kwarsg['btn_text'])
		except KeyError:
			self.applypage.click_sublimeApply("通过")

		self.applypage.click_popWindow("确定")
		publicTool.wait_LoadingModal(self)

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		return self.mainpage.get_status(email)


	"""
		# 提交审核
		# 适用于未处理状态
		# 通过email,确定需要操作的数据
		# 勾选,点击提交审核按钮

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def submitReview(self, email, statusSel, *args, **kwarsg):
		publicTool.click_menulist(self, "开户管理", "开户列表")
		publicTool.wait_LoadingModal(self)

		# 下拉列表选择未处理
		self.mainpage.click_StatusSelect(statusSel)
		publicTool.wait_LoadingModal(self)

		# 判断状态校验功能是否正常,选择编号
		self.mainpage.click_checkbox(email=email)	
		self.mainpage.click_submitreview()
		self.applypage.click_popWindow("确定")
		publicTool.wait_LoadingModal(self)

		self.assertIsNot("待CS2审批", self.mainpage.get_status(email), "状态没有改变")
		# globals()["status"] = self.mainpage.get_status(self.gm.get_value("email"))

		return self.mainpage.get_status(email)
		
	"""
		# 拒绝数据
		# 适用于CS1, CS2, RO状态
		# 通过email,确定需要操作的数据
		# 双击进入Apply表单,点击拒绝按钮并选择拒绝原因

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def reviewRefuse(self, email, statusSel, *args, **kwarsg):
		publicTool.click_menulist(self, "开户管理", "开户列表")
		publicTool.wait_LoadingModal(self)
		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect(statusSel)
		publicTool.wait_LoadingModal(self)

		self.mainpage.get_apply(email=email)
		publicTool.wait_LoadingModal(self)
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')
		try:
			if kwarsg['btn_text']:
				self.applypage.click_sublimeApply(kwarsg['btn_text'])
		except KeyError:
			self.applypage.click_sublimeApply("拒绝")
			
		# 选择拒绝原因
		self.applypage.rejectReason("确定")
		publicTool.wait_LoadingModal(self)

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("拒绝", self.mainpage.get_status(self.gm.get_value("email")), "状态没有改变")
		return self.mainpage.get_status(email)


	"""
		# OPS审核通过
		# 适用于OPS状态
		# 通过email,确定需要操作的数据
		# 双击进入Apply表单,点击通过按钮并填写账户号码

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def reviewFinish(self, email, statusSel, *args, **kwarsg):
		publicTool.click_menulist(self, "开户管理", "开户列表")
		publicTool.wait_LoadingModal(self)

		self.mainpage.click_StatusSelect(statusSel)
		publicTool.wait_LoadingModal(self)

		self.mainpage.get_apply(email=email)
		publicTool.wait_LoadingModal(self)
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("完成")
		# self.applypage.send_accountNumber(randox=1)
		# 自动生成客户编号
		self.applypage.autoCreateAccountNO()
		publicTool.wait_LoadingModal(self)
		# 点击确认按钮,生成账户号
		self.applypage.createTradeAccount()
		# 选择优惠码
		self.applypage.send_promoCode()
		# 点击确认按钮
		self.applypage.ops_createNO()
		publicTool.wait_LoadingModal(self)

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertEqual("成功", self.mainpage.get_status(email), "状态没有改变")

		return self.mainpage.get_status(email)

	"""
		# 修改数据
		# 适用于可以修改的状态
		# 通过email,确定需要操作的数据
		# 双击进入Apply表单,点击通过按钮并填写账户号码

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def reviewUpdate(self, email, statusSel, *args, **kwarsg):

		publicTool.click_menulist(self, "开户管理", "开户列表")
		publicTool.wait_LoadingModal(self)
		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect(statusSel)
		publicTool.wait_LoadingModal(self)

		self.mainpage.click_checkbox(email=email)	#选择多选框
		self.mainpage.click_update()	#点击修改按钮
		publicTool.wait_LoadingModal(self)
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-update', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("提交")
		# 选择拒绝原因
		self.applypage.click_popWindow("确定")
		publicTool.wait_LoadingModal(self)

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")


if __name__ == '__main__':
	print("1111111111111111")


