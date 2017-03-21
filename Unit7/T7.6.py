#T7.6
def dicadd(engl,chin,leng):
    addlist=engl
    for i in chin:
        addlist+=':'
        addlist+=i
    addlist+='\n'
    f=open('dicmul.txt','a+')
    f.seek(0)
    for line in f:
        if line.split(':')[0] == engl:
            print('词典中已经存在这个单词，不需要再添加了')
            f.close()
            break
    else:
        print('已添加有{}个意思的单词{}到字典中.'.format(leng,engl))
        f.write(addlist)
        f.close()
    

def dicget(word):
    f=open('dicmul.txt','r')
    for line in f:
        if line.split(':')[0] == word:
            leng=len(line.split(':'))
            print('已从字典中找到{}这个词语,总共有{}个意思.'.format(word,leng-1))
            for i in range(leng-1):
                print('第{}个意思是{}.'.format(i+1,line.split(':')[i+1]),end='')
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
            leng=len(order.split(' ')) -2
            eng=order.split(' ')[1]
            eng.replace(' ','')
            dicadd(eng,order.split(' ')[2:],leng)
        elif mode =='查询':
            dicget(order.split(' ')[1])
        else:
            print("您输入的命令不存在.")



print("词典程序为您服务，请参见一下使用规则：")
print("+------------------------------------+")
print("|1.ADD方法：添加 英文单词 中文单词   |")
print("|如果要添加多个解释可以中间加上逗号  |")
print("|2.Get方法：查询 英文单词/中文单词   |")
print("|3.Quit方法： 退出                   |")
print("+------------------------------------+")
main()
#print('用户执行了错误的操作')
#main()

