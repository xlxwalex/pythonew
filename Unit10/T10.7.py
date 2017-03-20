#10.7
import requests
import bs4
import time

def baiduclock():
    tim=0
    agent={'User-agent':'Mozilla/5.0'}
    timer=time.clock()
    while time.clock() - timer <= 30:
        print(time.clock() - timer)
        httpbaidu=requests.get('http://www.baidu.com',headers=agent)
        if httpbaidu.status_code == 200:
            tim+=1
    else:
        print("30s内爬虫访问了百度{}次".format(tim))

baiduclock()
