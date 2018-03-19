# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 20:48
# @Author  : xxxz
# @File    : mydict.py
# @Software: PyCharm

# 可以通过属性访问的dict
class Dict(dict):

    def __init__(self, **kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key) #r -- raw string

    def __setattr__(self, key, value):
        self[key] = value