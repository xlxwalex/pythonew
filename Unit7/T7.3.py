#7.3
from PIL import Image
charlst=list('一二人八十三大六七四口')

def charget(r,g,b,alpha=256):
    if alpha == 0:
        return '*'
    #这里应用到了书中的彩色转灰度公式↓
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    unit=256/len(charlst)  #字符种类及rgb值对应
    return charlst[int(gray//unit)] #返回字符

def main():
    im=Image.open("pic.jpg") #测试用的jpg
    width,height=100,60
    im=im.resize((width,height))
    txt="" #定义输出的txt
    for i in range(height):
        for r in range(width):
            txt += charget(*im.getpixel((r,i)))
        txt += '\n'
        f = open('charpic.txt','wt')
        f.write(txt)
        f.close()
    return txt

print(main())
print('-----已成功生成-----')
