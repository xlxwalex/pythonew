#6.6 这里输出20个没有把无关词汇都排除，有兴趣的可以改改line3
from jieba import lcut
excludes=['什么','一个','我们','那里','你们','如今','说道','知道','不是','没有','两个','老太太']
txt = open("T6.6.txt","r", encoding = 'utf-8').read()
words=lcut(txt)
counts={}
for word in words:
    if len(word) != 1:
        counts[word]=counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)
for i in range(20):
    word,count =items[i]
    print("{0:<10}{1:>5}".format(word,count))
