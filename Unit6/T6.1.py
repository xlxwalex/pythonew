#6.1
from random import randint
def rancre():
    mi=''
    for i in range(8):
        u = randint(0,62)
        if u>=10:
            if 90<(u+55)<97:
                mi+=chr(u+62)
            else:
                mi+=chr(u+55)
            print("{} ".format(u+55),end="")           
        else:
            mi+='%d'%u
    return mi

def main():
    for i in range(1,11):
        print("生成的第{}个密码是：{}".format(i,rancre()))

main()
