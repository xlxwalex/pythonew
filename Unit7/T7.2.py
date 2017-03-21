#7.2
from PIL import Image
import os

def getsize(path):
    try:
        size=os.path.getsize(path)
        size = float(size)
        kb=size/1024
        per=10/kb
        chanpic(per,path)
    except:
        print("There is a error")
        
def chanpic(per,path):
    im=Image.open(path)
    imsize=im.size
    sizex=int(imsize[0]*per)
    sizey=int(imsize[1]*per)
    im=im.resize((sizex,sizey))
    im.save('trans.jpg','JPEG')
    print('图片转换完成，输出成功')
    print('{}->>({},{})'.format(imsize,sizex,sizey))
          
def main():
    #这里方便测试就指定了当前文件夹的图片，有需要可解锁input语句
    #path=input("请输入需要更改大小的图片的路径：")
    path='pic.jpg'
    getsize(path)

main()
