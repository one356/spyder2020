#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201209.py
    @time:2020/12/09
"""
# 示例
import pandas as pd
import akshare as ak
# 列名与数据对其显示
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sz399552")
with open('stock_zh.txt', 'w') as f:
    f.write(str(stock_zh_index_daily_df))