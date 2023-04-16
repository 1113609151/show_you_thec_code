
import random
import string
import os

words = []

# 生成随机单词
for i in range(1000):
    word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
    words.append(word)

# 将单词写入文件
with open('words.txt', 'w') as file:
    file.write(' '.join(words))