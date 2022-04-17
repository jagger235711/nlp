"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/24 16:06

 @Author : jagger

 @File : 绘制柱状图.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

"""
# coding:utf-8
__author__ = 'similarface'

import numpy as np, array
from matplotlib import pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(9, 6))
X = [str(i) for i in np.arange(22) + 1] + ['X', 'Y', 'MT']
Y = np.array([196416, 289003, 70031, 411185, 79632, 394154])
plt.bar(np.arange(6) + 0.1, Y, width=0.3, facecolor='green', edgecolor='white')
plt.xticks(np.arange(6), ['P_0_0.05', 'P_0.05_1', 'w_0_0.05', 'w_0.05_1', '23me_0_0.05', '23me_0.05_1'])
k = [902676.0, 902676.0, 596768.0, 596768.0, 610565.0, 610565.0]
i = 0
X = np.arange(6)
for x, y in zip(X, Y):
    plt.text(x + 0.25, y + 0.1, '%.2f' % (y * 100 / k[i]) + "%", ha='center', va='bottom')
    i = i + 1
plt.xlabel(u"频率标志")
plt.ylabel("Number of Markers")
plt.title(u"PMRA wegene 23andme 频率分布")
plt.show()
