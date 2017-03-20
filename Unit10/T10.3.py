#T10.3 爬取bilibili视频
import requests
import re
import bs4
import re
av=input("请输入视频的AV号:")
url="http://www.ibilibili.com/video/av"+av+'/'
agent={'User-agent':'Mozilla/5.0'}
bilihtml=requests.get(url,headers=agent)
bilihtml.encoding=bilihtml.apparent_encoding
soup=bs4.BeautifulSoup(bilihtml.text,'html.parser')
rule='[0-9]*'
for i in soup.find_all('a'):
    if 'onclick' in i.attrs:
        ider=i.attrs.get('onclick')
ruler=re.compile(rule)
videourl='http://cn-sdyt-cu-v-07.acgvideo.com/vg3/1/c8/'+re.findall(ruler,ider)[7]+'-1-hd.mp4'
print('得到的视频Url为：',videourl)        
        


