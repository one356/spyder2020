#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201120.py
    @time:2020/11/20
"""
# 爬取搜狗首页
import requests as rq
if __name__ == '__main__':
    # 1,指定url地址
    url = 'https://www.sogou.com/'
    # headers = {'User-Agent':}
    # 2.发起get或者post请求
    response = rq.get(url=url)
    # 3.获取响应数据
    print(response.text)
    # 4,持久化存储
    with open('./sogou.html',mode='w',encoding='utf-8') as fp:
        fp.write(response.text)
