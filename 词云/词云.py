"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/24 14:37

 @Author : jagger

 @File : 词云.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

"""
import jieba
import imageio
import matplotlib.pyplot as plt  # 数学会图库
from wordcloud import WordCloud

filename = "政府工作报告2021.txt"
inputs = open(filename, 'r', encoding='UTF-8')
wordF = {}


def stopwordslist():
    stopwords = [line.strip() for line in open('chinsesstoptxt.txt', encoding='UTF-8').readlines()]
    return stopwords


def seg_depart(sentence):
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
    outstr += " "
    return outstr


for line in inputs:
    line_seg = seg_depart(line)
    word_list = jieba.cut(line_seg)
    line_seg = ' '.join(word_list)
    word_list = jieba.cut(line_seg)
    for word in word_list:
        if wordF.get(word) is None:
            wordF[word] = 1
        else:
            wordF[word] += 1
inputs.close()
wordF.pop(" ")
wordF.pop("，")
wordF.pop("：")
wordF.pop("。")
# 设置词云
color_mask = imageio.imread("time.jpg")
wc = WordCloud(background_color="white",  # 设置背景颜色
               mask=color_mask,
               max_words=200,  # 设置最大显示的字数
               # stopwords = "", #设置停用词
               font_path="simfang.ttf",
               # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文），不加这个的话显示口型乱码
               max_font_size=100,  # 设置字体最大值
               random_state=50,  # 设置有多少种配色方案
               margin=2,
               )
myword = wc.generate_from_frequencies(wordF)
# 展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()
