#从文件夹diary中，读取每个txt中的内容，并找出每个文件最重要的词
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict


def solution():

    

    stop_words = set(stopwords.words('english'))

    #读取diary中存在的文件
    files = os.listdir('./diaries')

    diaries = []
    #遍历每个文件
    for file in files:
        #打开文件
        with open('./diaries/'+file, 'r') as f:
            #读取文件中的内容
            content = f.read()
            diaries.append(content)

    # 统计词频
    word_freq = defaultdict(int)

    for diary in diaries:
        # 分词
        words = word_tokenize(diary.lower())
        # 去除停用词和标点符号
        words = [word for word in words if word.isalnum() and word not in stop_words]
        # 统计词频
        for word in words:
            word_freq[word] += 1


    # 计算词的重要性得分
    word_scores = {}
    total_diaries = len(diaries)
    for word, freq in word_freq.items():
        # 使用简单的词频作为重要性得分
        score = freq / total_diaries
        word_scores[word] = score

    # 获取每篇日记的最重要词
    for i, diary in enumerate(diaries):
        words = word_tokenize(diary.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        words = list(set(words))
        most_important_word = sorted(words, key=lambda word: word_scores[word], reverse=True)
        print(f"Most important word in diary {i+1}: {most_important_word[0]}, {most_important_word[1]}, {most_important_word[2]}")

if __name__ == '__main__':
    # nltk.download('punkt')
    solution()