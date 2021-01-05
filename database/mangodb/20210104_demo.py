#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20210104_demo.py
    @time:2021/01/04
"""
# 读取文件并用pandas做简单分析
import pandas as pd

day_time = '2021-01-04'
if __name__ == '__main__':
    data = pd.read_csv('永安data%s.txt'%day_time)
    print(data)
