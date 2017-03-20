#T10.5 （Same as T10.4）
import requests
import bs4
import urllib.robotparser

def backhtml(url):
    htmlback=requests.get(url)
    htmlback_encoding=htmlback.apparent_encoding
    soup=bs4.BeautifulSoup(htmlback.text,'html.parser')
    print('网页代码如下：')
    print(soup.prettify())
    
def robotana(url,urlwant,strin):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url)
    rp.read()
    if rp.can_fetch("*", urlwant) == True:
        print('robots协议未禁止')
        backhtml('http://' + urlwant)
    else:
        print("十分抱歉，对方网页禁止了您的访问；请看以下规则")
        print(strin)
    
url=input("请输入您要爬取的网页,不用输'http'：")
realurl=url.split('/',1)[0]
roboturl='http://'+realurl+'/robots.txt'
robotread=requests.get(roboturl)
robotread.encoding=robotread.apparent_encoding
if robotread.status_code != 200:
    print('您爬取的网站没有设置robots规则，正在返回网页源代码')
    backhtml('http://'+url)
else:
    print("正在分析规则..")
    robotana(roboturl,url,robotread.text)
    

