#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201208.py
    @time:2020/12/08
"""
# 定义A类
# 在main()中调用A类中定义的函数
# 尽力在class中写方法，main()中简洁调用
class A(object):
    def __init__(self):
        pass

    def run(self):
        print('hello')


def main():
    # 创建一个对象
    a = A()
    # 运行对象
    a.run()


if __name__ == '__main__':
    main()
