#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201202.py
    @time:2020/12/02
"""
# 网页图片的爬取
import requests
if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    print(page_text)
