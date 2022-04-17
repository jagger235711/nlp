"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/10 22:08

 @Author : jagger

 @File : jieba.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

"""
import jieba
import jieba.posseg as pseg  # 词性标注
from collections import Counter

# # print(sourceTxt.read())
# jieba.load_userdict('myDic.txt')  # file_name 为文件类对象或自定义词典的路径 词语、词频（可省略）、词性（可省略）
# with open('一念永恒第 113 章 第120章 挑战白小纯！.txt', encoding='utf-8') as sourceTxt:
#     sourceTxt = sourceTxt.read()
#
#     # res = jieba.cut(sourceTxt)  # 返回的结构是一个可迭代的 generator
#     # # print('|'.join(res))
#     # # t = [(word, flag) for word, flag in res]  # 列表解析
#     # # print(t)
#     # for word, flag in pseg.cut(sourceTxt):
#     #     if word not in '|"#$%&()*+,-./:;<>+?@![\\]^_{|}~\n\t。， ':
#     #         print('%s %s' % (word, flag))
#
#     # for word, flag in pseg.cut(sourceTxt):
#     #     if word not in '|"#$%&()*+,-./:;<>+?@![\\]^_{|}~\n\t。，‘“”！ ':
#     #         print('|%s' % word, end='')
#
#     c=Counter(sourceTxt).most_common(20)
#     print(c)

with open('一念永恒/一念永恒第 11 章 第十一章 侯小妹.txt', encoding='utf-8') as a:
    print(a.read())
