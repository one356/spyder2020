#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201122.py
    @time:2020/11/22
"""
import requests
import json
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    # 输入要查询的内容
    keyword = input('请输入要查询的单词：')
    data_kw = {
        'kw':keyword
    }
    response = requests.post(url=post_url,data=data_kw,headers=headers)
    dic_obj = response.json()

    print(dic_obj)
    file_name = keyword+'.json'
    fp = open(file_name,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('完成')
