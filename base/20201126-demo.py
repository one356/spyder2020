#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201126-demo.py
    @time:2020/11/26
"""
# 列表 list
if __name__ == '__main__':
    # 第一种
    lst = ['hello','world',98]
    # 第二种
    lst2 = list(['hello',88,'world'])
    print(lst,lst2)
    #列表方法
    #     定位列表元素位置
    print(lst.index('hello',0,1))
    #     获取列表中的元素
    print(lst[2])
    print(lst[-3])
    print(lst[1:])
    print(lst[:1])
    print(lst[-1:])
    print(lst[:-2])
    print(lst[0:2:2])
    #    判断列表元素 in,not in
    print('hello' in lst)
    print('hello' not in lst)

    #   列表遍历 for 迭代变量 in 列表名 :
    for item in lst:
        print(item)
    #   列表元素操作
    lst.append('addword')
    print(lst)
    lst.extend('abcdef')    #iterable可迭代对象
    print(lst)
    lst.insert(1,22)
    print(lst)
    lst[1:] = lst2  #切片是产生新对象
    print(lst)
    lst.remove('hello') #删除
    print(lst)
    lst.pop(1)  #根据索引index删除
    print(lst)
    lst2[1:2] = []  #不产生新对象列表
    print(lst2)
    # lst2.clear()    #清空列表
    # del lst2    #删除列表
    lst[1] = 20     #单独元素修改
    print(lst)
    lst2[0:1] = [200,2]     #利用切片批量修改
    print(lst2)
    #lst2.sort(reverse=True)     #reverse降序排序
    print(lst2)
    lst4 = [i for i in range(1, 10)]    #生成列表
    print(lst4)









