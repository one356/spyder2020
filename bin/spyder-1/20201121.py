#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201121.py
    @time:2020/11/21
"""
import requests
if __name__ == '__main__':
    # 将原url = 'https://www.sogou.com/web?query=python'中通过params参数调用
    url = 'https://www.sogou.com/web'
    #处理url携带参数，封装到字典中
    kw = input('输入关键字：')
    param = {
        'query':kw
    }
    # UA参数伪装为浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers,params=kw)
    page_text = response.text
    # print(page_text)
    filename = kw+'.html'
    # 写入filename.html
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'保存成功')



    









