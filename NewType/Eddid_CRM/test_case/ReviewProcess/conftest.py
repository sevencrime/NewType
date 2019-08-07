#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class TestExample(object):

    def setup(self):
        print("setUp4444444444444444444444")

    def teardown(self):
        print("tearDown77777")

    @pytest.mark.dependency()
    def test_a(self):
        print("aaaaaaaaaaaaaaaa")
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        print("bbbbbbbbbbbbbbbbb")
        assert False

    @pytest.mark.dependency(depends=["TestExample::test_a"])
    def test_c(self):
        # TestExample::test_a 没通过则不执行该条用例
        # 可以跨 Class 筛选
        print("Hello I am in test_c")

    @pytest.mark.dependency(depends=["TestExample::test_a","TestExample::test_b"])
    def test_d(self):
        print("Hello I am in test_d")


if __name__ == '__main__':
    pytest.main(["-s", "conftest.py"])