#6.5
from random import *

def randbirth():
    mon=randint(1,12)
    if mon in[1,3,5,7,8,10,12]:
        day=randint(1,31)
    elif mon ==2:
        day=randint(1,28)
    else:
        day=randint(1,30)
    return mon*100+day
    
def main():
    ls=[]
    for i in range(23):
        ls.append(randbirth())
    if len(ls) == len(set(ls)):
        return 1
    else:
        return 0

try:
    poss=0
    n=eval(input("请输入样本数量："))
    for i in range(n):
        if main() == 1:
            poss+=1
    if (poss/n) >= 0.5:
        print("当房间内的人数为23人时，他们生日几率超过了50%,是{}%".format(poss*100/n))
    else:
        print("当房间内的人数为23人时，他们生日几率没有一半,是{}%".format(poss*100/n))

               
except:
    print("输入有误")


