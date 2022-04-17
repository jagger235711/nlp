"""
 -*- coding: utf-8 -*-

 @Time : 2022/3/29 18:39

 @Author : jagger

 @File : 共现关系统计.py

 @Software: PyCharm 

 @contact: 252587809@qq.com

 -*- 功能说明 -*-

"""


# 将剧本进行分词，并将表示人名的词提出，将其他停用词和标点省略
# 提出人名的同时，同name字典记录下来，作为矩阵的行和列
def cut_word(text):
    words = pseg.cut(text)
    L_name = []
    for x in words:
        if x.flag != 'nr' or len(x.word) < 2:
            continue
        if not Names.get(x.word):
            Names[x.word] = 1
        else:
            Names[x.word] = Names[x.word] + 1
        L_name.append(x.word)
    return L_name


# 建立词频字典和每段中的人物列表
def namedict_built():
    global Names
    with open('e:/PY/relationship_find/test.txt', 'r') as f:
        for l in f.readlines():
            n = cut_word(l)
            if len(n) >= 2:  # 由于要计算关系，空list和单元素list没有用
                Lines.append(n)
    Names = dict(sorted(Names.items(), key=lambda x: x[1], reverse=True)[:36])
    # print(Line)


# 通过遍历Lines来构建共现矩阵
def relation_built():
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
