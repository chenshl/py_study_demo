#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""mydict的单元测试"""
__author__ = "chensl"

import unittest
from Study.StudyTwo.mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        print("连接数据库成功。。。")

    def tearDown(self):
        print("关闭数据库成功。。。")

    def test_init(self):
        print("1")
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertEqual(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")
        print("2")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")
        print("3")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]
        print("4")

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
        print("5")


if __name__ == "__main__":
    unittest.main()
