#10.6   分析得到的api接口：https://image.baidu.com/search/index?tn=baiduimage&word=
import requests
import bs4
import re

def picurlget(word):    
    agent={'User-agent':'Mozilla/5,0'}
    key={'word':word}
    link_urls=[]
    baihtml = requests.get("https://image.baidu.com/search/index?tn=baiduimage",params=key,headers=agent)
    baihtml.encoding = baihtml.apparent_encoding
    #Re规则只写了三个，有兴趣可以自己添加
    obeyurl=['http:\/\/[^\s,"]*\.jpg','http:\/\/[^\s,"]*\.jpeg','http:\/\/[^\s,"]*\.png']
    for li in obeyurl:
        baiurl = re.compile(li)
        link_urls+=re.findall(baiurl, baihtml.text)
    return link_urls

def downpic(url,path,contenter):
    with open(path,'wb') as filer:
        filer.write(contenter)
        filer.close()
        print("已经保存照片到{}".format(path))
    
def main():
    word=input("请输入您自己准备下载的图库名称 ：")
    urllist=picurlget(word)
    for ur in urllist:
       path="pics/"+ur.split('/')[-1]
       con=requests.get(ur)
       downpic(ur,path,con.content)
       
main()
    

