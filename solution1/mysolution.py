# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 21:03
# @Author  : xxxz
# @File    : mysolution.py
# @Software: PyCharm

import re


class Solution:

    def isvalid(self, str1):

        # isalnum
        # 出现1次或多次非数字字母字符，或空字符串
        p = re.compile('([\W]+)|^$')

        if p.search(str1) is None:
            return True
        else:
            return False


    # 从左开始比较子串
    def cmpsubstrfromleft(self, str1, str2):

        p = re.compile('[\d]+|[a-zA-Z]+')
        leftsubstr1 = p.findall(str1)[0]
        leftsubstr2 = p.findall(str2)[0]

        # base case
        if leftsubstr1=='' and leftsubstr2=='':
            return 0

        if self.cmpstr(leftsubstr1, leftsubstr2):       # 如果左子串不等, 返回比较结果
            return self.cmpstr(leftsubstr1, leftsubstr2)
        else:                                           # 如果左子串相等，继续比较下一子串
            return self.cmpsubstrfromleft(str1.lstrip(leftsubstr1), str2.lstrip(leftsubstr2))

    # 比较字符串
    def cmpstr(self, str1, str2):

        if str1=='' and str2=='':
            return 0
        elif str1=='':
            return 1
        elif str2=='':
            return 2


        if str1.isdigit() and str2.isdigit():
            return self.numbercmp(str1, str2)

        elif str1.isdigit() and str2.isalpha():
            return -1

        elif str1.isalpha() and str2.isdigit():
            return -2

        else:
            return cmp(str1, str2)


    def numbercmp(self, str1, str2):
        if int(str1)>int(str2):
            return 1
        elif int(str1)<int(str2):
            return -1
        else:
            return cmp(len(str1),len(str2))
