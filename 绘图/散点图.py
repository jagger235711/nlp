"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/29 10:53

 @Author : jagger

 @File : 散点图.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

孩子年龄：22.32.52.72.93.03.33.53.94.04.24.34.4
4.64.95.0
孩子身高：7.79.19.09.39.69.69.19.68.99.19.49.61010
11.511.6
"""
# import matplotlib.pyplot as plt
# from numpy.random import rand
#
# fig, ax = plt.subplots()
# for color in ['red', 'green', 'blue']:
#     n = 750
#     x, y = rand(2, n)
#     scale = 200.0 * rand(n)
#     ax.scatter(x, y, c=color, s=scale, label=color,
#                alpha=0.3, edgecolors='none')
#
# ax.legend()
# ax.grid(True)
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# def drawStar():
#     plt.figure(figsize=(8, 4))
#     x = np.random.random(100)  # 生成100个0-1之间的数
#     y = np.random.random(100)
#     plt.scatter(x, y, s=x * 1000, c='y', marker=(5, 1), alpha=0.5, lw=2, facecolors='none')
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#
#     plt.show()


# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def draw1():
    plt.figure(figsize=(8, 4))
    # x = np.random.random(100)  # 生成100个0-1之间的数
    # y = np.random.random(100)
    y = [2, 2.3, 2.5, 2.7, 2.9, 3.0, 3.3, 3.5, 3.9, 4.0, 4.2, 4.3, 4.4,
         4.6, 4.9, 5.0]  # 年龄
    x = [7.7, 9.1, 9.0, 9.3, 9.6, 9.6, 9.1, 9.6, 8.9, 9.1, 9.4, 9.6, 10, 10,
         11.5, 11.6]  # 身高
    plt.scatter(x, y, c='y', alpha=1, lw=2, facecolors='none')
    plt.xlim(7, 12)
    plt.xlabel('身高')
    plt.ylabel('年龄')
    plt.ylim(1, 6)

    plt.show()


def draw2():
    x = [75, 87.2, 95.6, 103.1, 110.2, 116.6, 122.5, 128.5, 134.1, 140.1, 146.6, 152.4, 156.3, 158.6, 159.8, 160.1,
         160.3, 160.6]
    y = [9.40, 11.92, 14.13, 16.17, 18.26, 20.37, 22.64, 25.25, 28.19, 31.76, 36.10, 40.77, 44.79, 47.83, 49.82, 50.81,
         51.20, 51.41]
    a = [76.5, 88.5, 96.8, 104.1, 111.3, 117.7, 124.0, 130.0, 135.4, 140.2, 145.3, 151.9, 159.5, 165.9, 169.8, 171.6,
         172.3, 172.7]
    b = [10.01, 12.54, 14.65, 16.64, 18.98, 21.26, 24.06, 27.33, 30.46, 33.74, 37.69, 42.49, 48.08, 53.37, 57.08, 59.35,
         60.68, 61.40]
    plt.scatter(x, y, c='r', marker='o')
    plt.scatter(a, b, c='b', marker='*')
    plt.show()


draw2()
