# 实现功能

## 小说分词

## 分词词频

## 分词词性

    save_as_file(extract_keywords_frequency(), 'frequency')#获取小说分词、词频词性并保存

![img.png](img.png)

## 小说人物出场次数排序

    extract_keywords_figure()  # 小说人物出场次数排序

![img_1.png](img_1.png)
做了基本的筛选，后期文本量大的时候再根据出现次数限制一下，即可剔除不必要数据

## 小说人物共现关系提取

###不完整。
####主要思路：
1、读取人物列表构建有向人物关系矩阵\
2、按句子遍历语料，提取每句话里的姓名。每句话的名字分别保存到一个列表中\
3、用嵌套的for循环遍历，在矩阵对应位置加一\
4、排除主对角线（排除回环边）\
5、将矩阵中的关系转存到字典中排序

## 数据可视化

    draw_wordcloud(extract_keywords_figure())#人物关系可视化

![img_2.png](img_2.png)

## 数据保存功能

    # save_as_file(extract_keywords_frequency(), 'frequency')  # 获取小说分词、词频词性并保存

![img_3.png](img_3.png)
