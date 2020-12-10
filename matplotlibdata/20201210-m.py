#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:20201210-m.py
    @time:2020/12/10
"""
# matplotlib绘图示例
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
# 解决中文问题
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/Microsoft YaHei UI/simkai.ttf")
# 定义xy轴，都是可迭代对象
x = range(2,26,2)
y =np.random.randint(10,size=12)
# 设置大小和清晰度
plt.figure(figsize=(20,8),dpi=80)
# 绘制图片
plt.plot(x,y)
# 设置x轴刻度,参数是可迭代，y轴相同原理
plt.xticks(x,rotation=45)
# 描述x轴和y轴中的信息及标题
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度')
plt.title('时间温度表')
# 保存图片
plt.savefig("./sig_size.jpg")
plt.savefig("./sig_size.svg") #矢量图放大不会失真
# 展示图片
plt.show()

