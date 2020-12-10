#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201209-pandas-demo.py
    @time:2020/12/09
"""
# pandas demo
import pandas as pd

fpath = "./a.csv"
ratings = pd.read_csv(fpath)
ratings.head()
ratings.shape
