#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201213-demo.py
    @time:2020/12/13
"""

if __name__ == '__main__':
    def calc(a,b):
        c = a+b
        return c
    result = calc(10,20)
    print(result)

    # 判断是否是奇偶数
    def fun(num):
        odd=[] # 存放奇数
        even=[] # 存放偶数
        for i in num:
            if i%2:
                even.append(i)
            else:
                odd.append(i)
        return odd,even
    st_list=[11,22,14,23,46,75]
    print(fun(st_list))

    # 参数定义
    def fun2(a,b=10):   # b指定默认值
        print(a,b)
    fun2(100)
    fun2(20,30) # 默认值被替换

    # 个数可变的位置参数
    def fun3(*args):
        print(args)
    fun3(10)
    fun3(10,20,30)

    # 个数可变的关键字形参
    def fun4(**kwargs):
        print(kwargs)
    fun4(a = 10)
    fun4(a = 20,b = 30,c = 40)

