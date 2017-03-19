#5.4
def multi(n):
    num=1
    for i in n:
        num*=i
    return num

try:
    nu=list(eval(input("请输入任一组数的数据，用 , 隔开：")))
    print(multi(nu))
except:
    print("您输入的有错误")
    

