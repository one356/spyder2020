#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201224_demo.py
    @time:2020/12/24
"""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient(host="127.0.0.1",port="27017" )
    collection = client["Da"]
