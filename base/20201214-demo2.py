#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201214-demo2.py
    @time:2020/12/14
"""
# 类创建
class Student:
    native_place='辽宁'
    def __init__(self,name,age):    # name,age为实例属性
        self.name=name
        self.age=age
    # 实例方法
    def info(self):
        print('我的名字：',self.name,'我的年龄：',self.age)
    # 类方法
    @classmethod
    def cm(cls):
        print('类方法')
    # 静态方法
    @staticmethod
    def sm():
        print('静态方法')
stu = Student('张三',20)
print(stu)
print(stu.info)
print(stu.native_place)
Student.info(stu)


