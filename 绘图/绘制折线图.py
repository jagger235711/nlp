"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/24 14:52

 @Author : jagger

 @File : 绘制折线图.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

"""
import string
from matplotlib import pyplot as plt
import numpy as np

years = []
price = []
file = open('三国人物频率.txt', 'r')
lineList = file.readlines()
for line in lineList:
    lineList = line.strip().split(',')
file.close()
print(lineList)
for x in range(0, 6, 2):
    price.append(lineList[x])
print(years)
for y in range(1, 6, 2):
    price.append(lineList[y])
print(price)
plt.plot(years, price, 'b*')
plt.plot(years, price, 'r')
plt.xlabel('years+2000')
plt.ylabel('housing_average_price(*2000)')
plt.ylim(0, 15)
plt.title('line_regression&gradient decrease')
plt.legend('666')
plt.show()
