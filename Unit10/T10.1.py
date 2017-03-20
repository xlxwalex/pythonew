#T10.1
import requests
from bs4 import BeautifulSoup
import bs4
 
def getrankhtml(url):
    try:
        htmler = requests.get(url)
        htmler.raise_for_status()
        htmler.encoding = htmler.apparent_encoding
        return htmler.text
    except:
        print("当前网络出现了问题，请稍后重试")
 
def insertuniver(unilist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            unilist.append([tds[0].string, tds[1].string])
     
def main():
    ok=0
    print("正在加载大学列表...")
    univerlist = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getrankhtml(url)
    insertuniver(univerlist, html)
    finder=input("请输入您要寻找的大学：")
    for uni in univerlist:
        if uni[1] == finder:
            print("{}的排名是：{}".format(uni[1],uni[0]))
            ok=1
        else:
            continue
    if ok ==0 :
        print("未找到输入学校的信息")

main()
