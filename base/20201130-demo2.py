#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201130-demo2.py
    @time:2020/11/30
"""
# 集合
if __name__ == '__main__':
#     集合创建两种方式
    s1 = {1,2,2,3,3,4,5,6,7}
    print(s1)
    s2 = set(range(6))
    print(s2)
#     空集合
    s3 = set()
    print(s3)
#     集合操作
#     集合元素的判断 in/not in
    print(7 in s1)
    print(10 in s1)
    print(7 not in s1)

#     集合元素的新增操作
#       add()一次添加一个元素，update()至少添中一个元素
#       集合名不可以直接赋值命名 todo
#     s6 = s1.add(80) #不可以直接命名成s6
    s1.add(80)
    print(s1)
    s6 = s1
    print(s6)
    s2.update({'python',200,1000})
    print(s2)
#     集合元素的删除操作
#       remone()一次删除一个指定元素，如果指定元素不存在抛出KeyError
    s2.remove(200)
    print(s2)
#       discard()方法，一次删除一个指定元素，如果元素不存在抛出异常
    s2.discard(20)
    print(s2)
#       pop()方法，一次只删除一个任意元素
    s2.pop()    #不能添加参数
    print(s2)
#       clear()方法，清空集合
    s2.clear()
    print(s2)

