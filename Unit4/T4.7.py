#4.7
from random import randint
num=randint(1,10)
tim=0
while 1:
    try:
        putnum=eval(input("请输入您猜测的数字："))
        tim+=1
        if putnum > num:
            print("遗憾！太大了")
        elif putnum <num:
            print("遗憾！太小了")
        elif putnum==num:
            print("预测{}次，你猜中了！".format(tim))
            break
    except:
        print("输入有误！")
