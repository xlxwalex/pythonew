#T7.5
def dicadd(engl,chin):
    addlist=engl+':'+chin+'\n'
    f=open('dic.txt','a+')
    f.seek(0)
    for line in f:
        if line.split(':')[0] == engl:
            print('词典中已经存在这个单词，不需要再添加了')
            f.close()
            break
    else:
        print('已添加单词{}到字典中.'.format(engl))
        f.write(addlist)
        f.close()
    

def dicget(word):
    f=open('dic.txt','r')
    for line in f:
        if line.split(':')[0] == word:
            print('已从字典中找到{}这个词语，意思是{}'.format(word,line.split(':')[1]),end='')
            break
    else:
        print('字典中未找到这个词语')
    f.close()
    
    
def main():
    while 1:
        order=input("请输入您所需的操作命令：")
        mode = order.split(' ')[0]
        if mode == '退出':
            print('已经退出字典')
            break
        elif mode =='添加':
            eng=order.split(' ')[1]
            eng.replace(' ','')
            dicadd(eng,order.split(' ')[2])
        elif mode =='查询':
            dicget(order.split(' ')[1])
        else:
            print("您输入的命令不存在.")



print("词典程序为您服务，请参见一下使用规则：")
print("+------------------------------------+")
print("|1.ADD方法：添加 英文单词 中文单词   |")
print("|2.Get方法：查询 英文单词/中文单词   |")
print("|3.Quit方法： 退出                   |")
print("+------------------------------------+")
try:
    main()
except:
    print('用户执行了错误的操作')
    main()
