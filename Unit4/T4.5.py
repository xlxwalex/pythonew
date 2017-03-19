#4.5
#4.4
from random import *
import types
seed(100)
num=randint(0,100)
tim=0
while 1:
    try:
        putnum=eval(input("请输入您猜测的数字："))
        if type(putnum) == type(1):
            tim+=1
            if putnum > num:
                print("遗憾！太大了")
            elif putnum <num:
                print("遗憾！太小了")
            elif putnum==num:
                print("预测{}次，你猜中了！".format(tim))
                break
        else:
            print("输入内容必须为整数！")
    except:
        print("输入有误！")

