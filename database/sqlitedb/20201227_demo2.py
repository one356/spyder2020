#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201227_demo2.py
    @time:2020/12/27
"""
import sqlite3
db_file = 'test1.sqlite'
# 插入数据
def insert_score_data():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    insert_sql = 'insert into main_id (name,macth,chinese) values(?,?,?)'
    data = ('张三',79,87)
    cur.execute(insert_sql,data)
    conn.commit()
    cur.close()
    conn.close()
# 删除数据
def delete_score_data():
    conn = sqlite3.Connection(db_file)
    cur = conn.cursor()
    delete_sql = 'delete from main_id where id=?'
    data = (1,)
    cur.execute(delete_sql,data)
    conn.commit()
    cur.close()
    conn.close()
# 修改数据
def update_score_data():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    update_sql = 'update main_id set macth = ? , chinese = ? where id = 2'
    data = (99,99,)
    cur.execute(update_sql,data)
    conn.commit()
    cur.close()
    conn.close()
# 查询数据
def search_score_data():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    search_sql = 'select * from main_id'
    cur.execute(search_sql)
    print(cur.fetchall())
    cur.close()
    conn.close()
# 插入多条数据

    

if __name__ == '__main__':
    # insert_score_data()
    # delete_score_data()
    # update_score_data()
    search_score_data()