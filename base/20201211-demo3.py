#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201211-demo3.py
    @time:2020/12/11
"""
# 字符串
import sys
if __name__ == '__main__':
    # 强制驻留，默认pycharm会优化驻留机制，额
    a = 'abc%'
    b = 'abc%'
    a = sys.intern(b)
    print(a is b)
