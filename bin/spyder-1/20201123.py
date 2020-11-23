#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201123.py
    @time:2020/11/23
"""
# 抓取豆瓣电影
import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',
        'limit': '20',
    }
    headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
               }
    response = requests.get(url=url,headers=headers,params=param)
    list_data = response.json()
    fp = open('./movice.json','w',encoding='utf-8')
    # 转换成字典
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('完成')
    
    
