# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 21:07
# @Author  : xxxz
# @File    : mysolution_test.py
# @Software: PyCharm

import unittest
from mysolution import Solution


class TestSolution(unittest.TestCase):

    def test_isvalid(self):
        solution = Solution()
        self.assertTrue(solution.isvalid('111'))
        self.assertTrue(solution.isvalid('111aaa'))
        self.assertTrue(solution.isvalid('aaa'))
        self.assertFalse(solution.isvalid(''))
        self.assertFalse(solution.isvalid('111*-*'))
        self.assertFalse(solution.isvalid('1a1s\n'))

    def test_numbercmp(self):
        solution = Solution()
        self.assertEquals(solution.numbercmp('123','456'), -1)
        self.assertEquals(solution.numbercmp('0123', '456'), -1)
        self.assertEquals(solution.numbercmp('123', '0123'), -1)
        self.assertEquals(solution.numbercmp('123', '123'), 0)
        self.assertEquals(solution.numbercmp('458', '132'), 1)

    def test_cmpsubstr(self):
        solution = Solution()
        self.assertEquals(solution.cmpsubstr('123', 'abc'), -1)
        self.assertEquals(solution.cmpsubstr('abc', 'bac'), cmp('abc','bac'))
        self.assertEquals(solution.cmpsubstr('abc', '123'), 1)
        self.assertEquals(solution.cmpsubstr('123', '0123'), -1)
        self.assertEquals(solution.cmpsubstr('', '132'), -1)

    def test_cmpfromleft(self):
        solution = Solution()
        self.assertEquals(solution.cmpfromleft('123','abc'),-1)
        self.assertEquals(solution.cmpfromleft('123abc','123abc'),0)
        self.assertEquals(solution.cmpfromleft('123abc','123abc1'),-1)
        self.assertEquals(solution.cmpfromleft('abc123','abc0123'),-1)

