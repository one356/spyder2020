#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201224_demo.py
    @time:2020/12/24
"""
from pymongo import MongoClient
import requests
import datetime
from bs4 import BeautifulSoup

# 数据库实例
class QhMongoDB:
    def __init__(self):
        # 建立连接到数据库
        client = MongoClient(host="127.0.0.1",port=27017)
        # 连接到指定qh表和ynqh集合
        collection = client["qh"]["ynqh"]
    # def qh_insert(self):    # 插入一条数据
        # ret = self.collection.insert()  # insert收取字典文件
        # print(ret)
    # def qh_insert_many(self):   # 插入多条数据
        # item_list =


# day_time = datetime.date.today()    #获取今天日期

day_time = "2020-12-30"    #获取今天日期
# 爬虫头信息
header = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.66Safari / 537.36"
        }
# 定义爬虫
class SpyderData:
    def spyder_data_all(self):  #爬取永安全部品种持仓
        self.url = "http://service.99qh.com/hold2/MemberGoodsHold/GetTableHtml.aspx?date=%s&mem=521&user=99qh&script=no" % (day_time,)  # 链接地址
        self.spyder_data_all_response =requests.get(url=self.url,headers=header).text   # 返回数据
        # 如果提前抓取有可能为空，返回提示
        if self.spyder_data_all_response != '':
            # print(self.spyder_data_all_response)
            print("已经链接！")
        else:
            print("没有访问到数据")
        soup = BeautifulSoup(self.spyder_data_all_response,'lxml')  # 解析抓取的数据
        # 获取表格中数据
        tables = soup.find_all('table')
        tab = tables[0]
        title_tr = soup.find_all('tr')[2]   # 定位标题名tr位置
        title_list = []
        for td in title_tr.find_all('td'):
            title_list.append(td.getText())
        print('标题列表：',title_list)
        i = 3
        for tr in tab.find_all('tr'):
            try:
                data_tr = soup.find_all('tr')[i]   # 定位数据tr位置
            except IndexError:
                continue
            data_list = []
            for td in data_tr.find_all('td'):
                data_list.append(td.getText())
            print('数据列表：',data_list)
            i += 1

    def spyder_data_build(self,kind):
        self.url = "http://service.99qh.com/hold2/BuildHold/GetTableHtml.aspx?date=%s&mem=521&agree=%s" % (day_time,kind)
        self.spyder_data_all_response =requests.get(url=self.url,headers=header).text
        print(self.spyder_data_all_response)

if __name__ == '__main__':
    data_all=SpyderData()   # 实例化对象
    data_all.spyder_data_all()  # 调用方法返回全部持仓数据
    # kind = input("请输入期货代码（如：c2105）:")
    # data_all.spyder_data_build(kind)