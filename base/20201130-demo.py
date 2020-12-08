#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201130-demo.py
    @time:2020/11/30
"""
# 元组操作
if __name__ == '__main__':
#     元组不可以修改增删改查
    '''
    可变序列：列表，字典
    '''

    '''
    不可变序列：字符串，元组
    '''

    # 创建元组三种方式
    t = ('python','hello',90)
    d = tuple(('python','aaa',1000))
    f = (10,)   # 如果只有一个元素要加逗号
    print(t,d,f)
    print(type(t),type(d),type(f))
#     如果元组中的元素是可变序列，则可以对元素修改，如果元素是不可变序列则元素本身不可以修改
    g = (20,[30,33],40)
    print(g)
    print(g[1])
    g[1].append(37)
    print(g)
#       元组的遍历
    for item in t:
        print(item)




