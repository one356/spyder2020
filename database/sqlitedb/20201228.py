#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201228.py
    @time:2020/12/28
"""
# 读取excel文件保存到sqlite3中
import sqlite3
import os
import pandas as pd

current_address = os.path.dirname(os.path.dirname(__file__))
db_address = os.path.join(current_address,"test1.sqlite")
excel_address = os.path.join(current_address,"永安持仓1.xls")
# 读取Excel数据
df = pd.read_excel(excel_address)
print(df)

table_name = "constants"
conn = sqlite3.connect(db_address)
cur = conn.cursor()

fields_name = "C, D"

for index, row in df.iterrows():
    a = row["A"]
    b = row["B"]
    fields_value = "'{0}', {1}".format(a, b)
    sql = "Insert Into {0} ({1}) Values({2})".format(table_name, fields_name, fields_value)

    cur.execute(sql)
    conn.commit()

conn.close()

