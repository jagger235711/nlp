"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/11 7:37

 @Author : jagger

 @File : 自然语言处理作业.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-
根据第1部分自然语言处理教学内容，请选择一本你喜欢的小说，利用上课讲的但不限于授课内容，对该小说进行分析。
比如分析该小说的分词，词频，词性，小说人物出场次数排序，小说中食物排序（这个得有，我喜欢吃），小说人物关系等等。

要求：1代码以py文件附件形式上传，有功能性注释和普通注释。

2.功能介绍和运行结果截图可以在作业里写上。

3.小说文件用txt形式存储。

4.最后视功能完整性给分。
"""
from os import listdir
import jieba
import jieba.posseg as pseg
import jieba.analyse as anl
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

'''
1、获取素材
filelist读取目录下所有txt文件
2、处理素材
    2.1分词
    2.2分词得词性
    2.3提取关键词
3、输出素材
'''
# 设置相关的文件路径
bg_image_path = "chinaMap.jpg"
text_path = '一念永恒第 4 章 第四章 炼灵.txt'
# text_path = '一念永恒全集.txt'
font_path = 'simfang.ttf'
stopwords_path = 'baidu_stopwords.txt'
userwoeds_path = 'myword.txt'


def clean_using_stopword(text):
    '''
    去除停顿词，利用常见停顿词表+自建词库

    Parameters
    ----------
    text :
     语料（str
    Returns
    -------
    '''
    mywordlist = []
    jieba.load_userdict(userwoeds_path)
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/".join(seg_list)
    with open(stopwords_path, encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):  # 去除停顿词，生成新文档
        if (not (myword.strip() in f_stop_seg_list)) and len(myword.strip()) > 1:  # 长度大于一且不在停用词表中
            mywordlist.append(myword)
    return ''.join(mywordlist)


def preprocessing():
    '''
    文本预处理

    Returns
    -------

    '''
    with open(text_path, encoding='utf-8') as f:
        content = f.read()
    return clean_using_stopword(content)
    # return content


def extract_keywords_frequency():
    """
    利用jieba来进行中文分词。
    analyse.extract_tags采用TF-IDF算法进行关键词的提取。
    :return:
    """
    # 抽取1500个关键词，带权重，后面需要根据权重来生成词云
    tags = jieba.analyse.extract_tags(preprocessing(), 1500, withWeight=True)
    keywords = dict()
    for i in tags:
        # print("%s---%f" % (i[0], i[1]))
        keywords[i[0]] = i[1]
    return keywords


def extract_keywords_tag():
    """
    利用jieba来进行中文分词。获取分词及其词性

    :return:
    """
    tags = pseg.cut(preprocessing())
    keywords = dict()
    for i in tags:
        if len(i.word) > 1:
            # print("%s---%s" % (i.word, i.flag))
            keywords[i.word] = i.flag
    return keywords


def extract_keywords_figure():
    '''
    分析主要出场人物并统计次数
    Parameters
    ----------

    Returns
    dic ['name':count]
    -------

    '''
    nameDic = {}
    Names = []
    with open('figure.txt', 'r', encoding='utf-8') as file:  # 读取人物列表,构建共现关系矩阵
        for line in file.readlines():
            name = (line.split()[0]).strip()
            Names.append(name)

    tags = pseg.cut(preprocessing())
    for i in tags:
        if not (len(i.word) > 1 and i.flag == 'nr'):
            continue
        if i.word in Names:
            if i.word == '小纯' or i.word == '白小纯':
                rword = '白小纯'
            elif i.word == '通天道人':
                rword = '杜天尊'
            else:
                rword = i.word
        else:
            rword = i.word
        # print("%s---%s" % (i.word, i.flag))
        nameDic[rword] = nameDic.get(rword,
                                     0) + 1  # 对key出现的频率进行统计，当key不在nameDic时，返回值是0，当key在nameDic中时，返回+1，以此进行累计计数
    items = list(nameDic.items())  # 字典到列表
    items.sort(key=lambda x: x[1], reverse=True)  # lambda是一个隐函数，是固定写法，以下命令的意思就是按照记录的第2列排序
    nameDic = dict(items)
    return nameDic


def extract_keywords_figure_paragraph():
    '''
    按句提取人物名字
    Returns
    -------

    '''


def co_occurrence():
    '''
    提取文章中的共现关系
    Returns
    -------

    '''
    Names = []
    with open('figure.txt', 'r') as file:  # 读取人物列表,构建共现关系矩阵
        for line in file.readlines():
            name = (line.split()[0]).strip()
            Names.append(name)


def relation_built():
    '''
    填充共现矩阵
    Returns
    -------

    '''
    for key in Names:
        relationships[key] = {}
    for line in Lines:
        for name1 in line:
            if not Names.get(name1):
                continue
            for name2 in line:
                if name1 == name2 or (not Names.get(name2)):
                    continue
                if not relationships[name1].get(name2):
                    relationships[name1][name2] = 1
                else:
                    relationships[name1][name2] = relationships[name1][name2] + 1
    # print(relationships)


def draw_wordcloud(dict):
    """
    生成词云。1.配置WordCloud。2.plt进行显示
    :return:
    """
    back_coloring = plt.imread(bg_image_path).astype(np.uint8)  # 设置背景图片
    # img = img.astype(np.uint8)

    # 设置词云属性
    wc = WordCloud(font_path=font_path,  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=2000,  # 词云显示的最大词数
                   mask=back_coloring,  # 设置背景图片
                   )

    # 根据频率生成词云
    wc.generate_from_frequencies(dict)
    # 显示图片
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    # 保存到本地
    wc.to_file("wordcloud.jpg")


def save_as_file(dic, filename):
    path = filename + '.txt'
    output = open(path, "ab")
    for first, second in dic.items():
        # print（t）
        output.write(first.encode('utf-8') + ' '.encode('utf-8') + str(second).encode('utf-8'))
        output.write('\n'.encode('utf-8'))
    output.close()


if __name__ == '__main__':
# save_as_file(extract_keywords_frequency(), 'frequency')  # 获取小说分词、词频词性并保存
# print(extract_keywords_figure())  # 小说人物出场次数排序
# draw_wordcloud(extract_keywords_figure())#人物关系可视化
