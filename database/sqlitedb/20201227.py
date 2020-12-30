#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201227.py
    @time:2020/12/27
"""


# sqlite模块使用

import sqlite3

if __name__ == '__main__':
    db_file = 'test.db' # 定义数据库路径
    conn = sqlite3.connect(db_file) # 连接数据库文件
    sql = 'select * from ser '  # 编写数据库sql语句
    cur = conn.cursor() # 执行sql语句
    cur.execute(sql)
    print(cur.fetchall())   #打印查询的结果
    conn.close()    # 关闭sql连接


