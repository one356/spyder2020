#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201127-demo.py
    @time:2020/11/26
"""

if __name__ == '__main__':
    scores = {'张三':22,'李四':32}
    print(scores)
    d = dict(a=25,b=21)
    print(d)
    # print(type(d))
    # 两种获取键值方式
    print(scores['张三'])
    print(scores.get('张三'))
    print(scores.get('玛琪'))
    # print(scores['玛琪'])这样会有报错
    # 键的判断
    print('张三' in scores)
    print('玛琪' not in scores)
    # 删除
    del scores['张三']
    print(scores)
    # 增加
    scores['陈六']=23
    print(scores)
    # 修改
    scores['陈六']=33
    print(scores)
#   视图操作共三种
    # 获取所有键
    keys = scores.keys()
    print(keys)
    print(type(keys))
    print(list(keys))
#     获取所有的值
    values = scores.values()
    print(values)
    print(type(values))
    print(list(values))
#     获取键值对
    items = scores.items()
    print(items)
    print(type(items))
    print(list(items))
#     遍历字典
    for i in scores:
        print(i)
    for item in scores:
        print(item,scores[item],scores.get(item))

#     字典特点
    d = {'name':'张三','name':'李四'}   #key值重复覆盖
    print(d)
    d = {'name':'张三','nikename':'张三'}   #value值可以重复
    print(d)
#     字典比较占用内存，是用空间换时间的方法

    #     字典生成函数zip（）
    item_books = ['fruits','books','others']
    prices = [96,78,85]
    e  = {item_book.upper():price for item_book,price in zip(item_books,prices)}
    print(e)




