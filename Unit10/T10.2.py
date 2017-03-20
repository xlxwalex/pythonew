#10.2
import requests
from bs4 import BeautifulSoup
import bs4
 
def unihtmlget(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "您的网络出现了一些问题"
 
def uninset(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
def outputuniv(ulist, num):
    tplt = "{0:^10}\t{1:^20}\t"
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1]))
     
def main():
    print("正在获取网络资源...")
    univerlist = []
    url = 'http://rankings.betteredu.net/usnews/global-universities/2016.html'
    html = unihtmlget(url)
    print("正在分析结果...")
    uninset(univerlist, html)
    outputuniv(univerlist, 40)
    
main()
