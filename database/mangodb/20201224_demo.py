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


class QhMongoDB:
    def __init__(self):
        client = MongoClient(host="127.0.0.1",port=27017)
        collection = client["qh"]["ynqh"]
    def qh_insert(self):
        # ret = self.collection.insert()  # insert收取字典文件 todo
        print(ret)
    def qh_insert_many(self):
        # item_list =
        pass


class SpyderData:

    def spyder_data_all(self):
        self.header = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.66Safari / 537.36"
        }
        self.day_time=datetime.date.today()
        self.url = "http://service.99qh.com/hold2/MemberGoodsHold/GetTableHtml.aspx?date=%s&mem=521&user=99qh&script=no" % (self.day_time,)
        self.spyder_data_all_response =requests.get(url=self.url,headers=self.header).text
        if self.spyder_data_all_response != '':
            print(self.spyder_data_all_response)
        else:
            print("没有访问到数据")
    def spyder_data_build(self,kind):
        self.header = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.66Safari / 537.36"
        }
        self.day_time = datetime.date.today()
        self.url = "http://service.99qh.com/hold2/BuildHold/GetTableHtml.aspx?date=%s&mem=521&agree=%s" % (self.day_time,kind)
        self.spyder_data_all_response =requests.get(url=self.url,headers=self.header).text
        print(self.spyder_data_all_response)

if __name__ == '__main__':
    data_all=SpyderData()
    data_all.spyder_data_all()
    kind = input("请输入期货代码（例如玉米c2105)：")
    data_all.spyder_data_build(kind)
