#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201214-demo.py
    @time:2020/12/14
"""
import traceback
# 异常处理
if __name__ == '__main__':
    print('两个数相加')
    try:
        a = int(input('输入a:'))
        b = int(input('输入b:'))
    except BaseException as e:
        print('输入错误请重试')
        print('错误：',e)
    else:
        print('a+b=',a+b)
    finally:
        print('谢谢使用')
    # 调用traceback模块返回错误信息，用于输出错误日志
    try:
        print('---------')
        print(1/0)
    except:
        traceback.print_exc()



