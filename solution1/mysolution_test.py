# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 21:07
# @Author  : xxxz
# @File    : mysolution_test.py
# @Software: PyCharm

import unittest
from mysolution import Solution


class TestDict(unittest.TestCase):

    def test_isvalid(self):
        solution = Solution()
        self.assertTrue(solution.isvalid('111'))
        self.assertTrue(solution.isvalid('111aaa'))
        self.assertTrue(solution.isvalid('aaa'))
        self.assertFalse(solution.isvalid(''))
        self.assertFalse(solution.isvalid('111*-*'))
        self.assertFalse(solution.isvalid('1a1s\n'))

    def test_strsplit(self):
        pass
