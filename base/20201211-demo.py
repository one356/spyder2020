#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201211-demo.py
    @time:2020/12/11
"""

# 集合操作

if __name__ == '__main__':
    s = {10,20,30,405,60}
    # 判断操作
    print(10 in s)
    print(100 in s)
    print(20 not in s)
    print(100 not in s)
    # 集合的添加操作
    s.add(89)
    print(s)
    s.update({40,45,405})
    print(s)
    s.update([22,33])
    print(s)
    # 集合删除操作
    s.remove(20)
    print(s)
    s.discard(30)
    print(s)
    s.pop()
    print(s)
    s.clear()
    print(s)


