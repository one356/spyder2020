#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201124-demo.py
    @time:2020/11/24
"""
# 逻辑运算符
if __name__ == '__main__':
    print('-------&按位与运算-----------')
    print('4&8 =',4&8)
    print('-------|按位或运算-----------')
    print('4|8 =', 4 | 8)
    print('-------<<左移位>>右移位运算-----------')
    # 左移和右移都是把数据转换成二进制计算
    # 每左移一个位置相当于原数据乘以2，n个位置相当于原数的n次方；右移相反。
    # 左移低位补零溢出舍弃，右移高位补零溢出舍弃。
    print('4<<1 =', 4 << 1)
    print('4>>1 =', 4 >> 1)
    #运算符优先级：算术运算符>位运算符>比较运算符>布尔运算符

    #对象的布尔值
    print(bool(False))
    print(bool(0))
    print(bool(0.0))
    print()
    '''
    任意程序都可以用三种结构包括：顺序，分支，循环。三种结构可以嵌套
        分支结构有以下几种：if 条件:            #1
                            pass
                        if 条件:              #2
                            pass
                        else 条件；
                            pass
                        if 条件:              #3
                            pass
                        elif 条件：
                            pass
                        elif 条件:
                            pass
                        else：
                            pass
                        #4条件表达式方式:为真输出if前执行；为假输出else后执行
                        print(a+'大于’+b if a>b else a+'小于等于'+b) 
                        
                        # pass语句是用于占位，不做任何操作                 
        
    '''

    '''
    # 循环
    1.range()函数
        用于生产一个整数序列
        有三种情况range(stop)/range(start,stop)/range(start,stop,step)
        
    2.while循环
    3.for-in循环--从in中依次取值遍历对象
    4.break、continue与else语句
    5.嵌套循环
    '''
    # demo_1
    r = range(5)
    print(list(r))
    r = range(1,5)
    print(list(r))
    r = range(1,5,2)
    print(list(r))
    #demo_2
    a = 1
    sum = 0
    while a<=100:
        if not bool(a%2):
            sum += a
        a += 1
    print(sum)
    #demo_3




