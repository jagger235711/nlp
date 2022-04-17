"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/11 7:33

 @Author : jagger

 @File : ppt程序.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

"""
import jieba
import jieba.analyse as anl
import jieba.posseg as pseg

# 导入用户自定义词典，注意必须是utf-8格式的
jieba.load_userdict("D:\\testpy\\userdict.txt")
# 1.读文件，分词，然后把分词结果存入另一个文件
# 第0步，遍历文件 
pathr = 'D:/testtxt/s'
pathw = 'D:/testtxt/s1'
# 第一步，打开学生的语料文件，然后分词
filenamer = pathr + '.txt'
article = open(filenamer, "r").read()
words = jieba.cut(article, cut_all=True)  # 全模式分词
# words = jieba.cut(article, cut_all = False)#精准模式分词
# words = jieba.cut_for_search(article)#搜索引擎模式分词
# words = jieba.cut(article)#默认精确模式分词
# 第二步，把分词后的结果存入txt文件中
f = " ".join(words)
filenamew = pathw + '.txt'
output_1 = open(filenamew, "w")
output_1.write(f.encode("utf-8"))
output_1.close()
# 2.分词得词性，然后输出分词结果
words = pseg.cut(article)  # 带词性的分词
filenamew = pathw + '2.txt'
output_2 = open(filenamew, "w")
for w in words:
    print
    w.word,
    print
    w.flag
    output_2.write(w.word.encode("utf-8"))
    output_2.write(w.flag.encode("utf-8"))
output_2.close()
# 3.提取关键字
tag = anl.extract_tags(article, 5)
filenamew = pathw + '3.txt'
output_3 = open(filenamew, "w")
for t in tag:
    print（t）
    output_3.write(t.encode("utf-8"))
output_3.close()
