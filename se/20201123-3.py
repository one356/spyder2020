#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201123-3.py
    @time:2020/11/23
"""
# 作业抓取se站
import requests
import time
import random
import os
#报错及检查无效页面 todo
if __name__ == '__main__':
    url = 'https://yj1.b96dure93e9.rocks/pw/read.php'
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.193Safari / 537.36'
    }
    # 设置抓取起止位置
    for kw in range(4042999,5059990):
        kw +=1
        # 开始时间输出
        print("Start : %s" % time.ctime())
        wait_time = random.randint(8,12)
        filename = str(kw)+'.html'
        print('当前开始页面：',filename,wait_time)
        if os.path.exists(filename):
            pass
        else:
            time.sleep(wait_time)
            param = {
                'tid' : kw
            }
            response = requests.get(url=url,params=param,headers=headers)
            # 从网页中获取网页编码方式，防止乱码
            response.encoding = response.apparent_encoding
            # 写入html文件保存
            filename = str(kw) + '.html'
            with open(filename,'w',encoding='utf-8') as fp:
                fp.write(response.text)
            print(filename,'已保存')
            # 输出时间
    print("End : %s" % time.ctime())







