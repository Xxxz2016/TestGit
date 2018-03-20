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
    def cmpfromleft(self, str1, str2):

        # base case
        if str1=='' and str2=='':
            return 0
        elif str1 == '':
            return -1
        elif str2 == '':
            return 1

        p = re.compile('[\d]+|[a-zA-Z]+')
        leftsubstr1 = p.findall(str1)[0]
        leftsubstr2 = p.findall(str2)[0]

        res = self.cmpsubstr(leftsubstr1, leftsubstr2)
        if res!=0:       # 如果左子串不等, 返回比较结果
            return res
        else:            # 如果左子串相等，继续比较下一子串
            return self.cmpfromleft(str1.lstrip(leftsubstr1), str2.lstrip(leftsubstr2))

    # 按规则比较子串
    def cmpsubstr(self, str1, str2):

        if str1=='' and str2=='':
            return 0
        elif str1=='':
            return -1
        elif str2=='':
            return 1

        if str1.isdigit() and str2.isdigit():
            return self.numbercmp(str1, str2)

        elif str1.isdigit() and str2.isalpha():
            return -1

        elif str1.isalpha() and str2.isdigit():
            return 1

        else:
            return cmp(str1, str2)

    # 比较数字子串
    def numbercmp(self, str1, str2):
        if int(str1)>int(str2):
            return 1
        elif int(str1)<int(str2):
            return -1
        else:
            return cmp(len(str1),len(str2))
