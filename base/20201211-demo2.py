#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201211-demo2.py
    @time:2020/12/11
"""
#集合之间的关系
if __name__ == '__main__':
    s1={10,20,30,40}
    s2={20,30,40,10}
    # 判断是否相等
    print(s1==s2)
    print(s1!=s2)
    print(s1.issubset(s2))
    print(s1.issuperset(s2))
    print(s1.isdisjoint(s2))
    # 数学操作
    # 交集
    s3={20,30,40,50,60}
    print(s1.intersection(s3))
    print(s1 & s3)
    #并集
    print(s1.union(s3))
    print(s1 | s3)
    #差集操作
    print(s1.difference(s3))
    print(s1 - s3)
    # 对称差集
    print(s1.symmetric_difference(s3))
    print(s1^s3)
    # 集合生成式
    s4 = {i*i for i in range(1,10)}
    print(s4)

    