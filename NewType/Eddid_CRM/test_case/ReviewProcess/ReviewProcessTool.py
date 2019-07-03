#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)
from PageElement import *
from Commons import *
from test_case.Test_Login import *
import unittest
from selenium import webdriver
import time
import pytest

class ReviewProcessTool(unittest.TestCase):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.set_page_load_timeout(20)
		self.driver.set_script_timeout(20)
		self.url = 'http://eddid-bos-uat.ntdev.be'

		# self.login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
		self.MenuListPage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
		self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

	def tearDown(self):
		# time.sleep(5)
		print("结束driver")
		self.driver.quit()

	# def skipIf(status):
	# 	# 装饰器, 用于判断用例是否执行
	# 	def wrapper(func):
	# 		def inner_wrapper(self):
	# 			if globals()['status'].find(status) != -1:
	# 				return func(self)
	# 			else:
	# 				print("状态不是 {}".format(status))
	# 				return 
	# 		return inner_wrapper
	# 	return wrapper

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
		self.MenuListPage.click_menulist("开户管理", "开户列表")
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect(statusSel)
		self.mainpage.wait_LoadingModal()

		self.mainpage.get_apply(email=email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
		# import pdb; pdb.set_trace()
		return self.mainpage.get_status(self.email)


	"""
		# 提交审核
		# 适用于未处理状态
		# 通过email,确定需要操作的数据
		# 勾选,点击提交审核按钮

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def submitReview(self, email, statusSel):
		self.MenuListPage.click_menulist("开户管理", "开户列表")
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择未处理
		self.mainpage.click_StatusSelect(statusSel)
		self.mainpage.wait_LoadingModal()

		# 判断状态校验功能是否正常,选择编号
		self.mainpage.click_checkbox(email=email)	
		self.mainpage.click_submitreview()
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
		# globals()["status"] = self.mainpage.get_status(self.email)

		return self.mainpage.get_status(self.email)
	"""
		# 拒绝数据
		# 适用于CS1, CS2, RO状态
		# 通过email,确定需要操作的数据
		# 双击进入Apply表单,点击拒绝按钮并选择拒绝原因

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def reviewRefuse(self, email, statusSel):
		self.MenuListPage.click_menulist("开户管理", "开户列表")
		self.mainpage.wait_LoadingModal()
		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect(statusSel)
		self.mainpage.wait_LoadingModal()

		self.mainpage.get_apply(email=email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		# 选择拒绝原因
		self.applypage.rejectRe
		ason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		return self.mainpage.get_status(self.email)


	"""
		# OPS审核通过
		# 适用于OPS状态
		# 通过email,确定需要操作的数据
		# 双击进入Apply表单,点击通过按钮并填写账户号码

		参数:
		email : 需要操作数据的email
		statusSel : 筛选状态select框
	"""
	def reviewFinish(self, email, statusSel):
		self.MenuListPage.click_menulist("开户管理", "开户列表")
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect(statusSel)
		self.mainpage.wait_LoadingModal()

		self.mainpage.get_apply(email=email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("完成")
		# self.applypage.send_accountNumber(randox=1)
		# 自动生成客户编号
		self.applypage.autoCreateAccountNO()
		self.mainpage.wait_LoadingModal()
		# 点击确认按钮,生成账户号
		self.applypage.createTradeAccount()
		# 选择优惠码
		self.applypage.send_promoCode()
		# 点击确认按钮
		self.applypage.ops_createNO()
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertEqual("成功", self.mainpage.get_status(self.email), "状态没有改变")

		return self.mainpage.get_status(self.email)