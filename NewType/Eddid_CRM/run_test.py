#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest import defaultTestLoader
import os

def get_TestCase():
	discover = unittest.defaultTestLoader.discover(os.getcwd(), pattern="test*.py")
	# print(discover)
	suite = unittest.TestSuite()
	suite.addTest(discover)
	return suite


if __name__ == '__main__':
	# get_TestCase()
	runner = unittest.TextTestRunner(verbosity=3)
	runner.run(get_TestCase())