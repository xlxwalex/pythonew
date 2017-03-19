#5.5
def Isprime(n):
    for i in range(2,n):
        for u in range(2,i):
            if i % u == 0:
                break
        else:
            print("{},".format(i),end="")  
               
                                    
def main():
    nu=eval(input("请输入您需要的质数范围:"))
    print("在1-{}中的质数有:".format(nu),end="")
    Isprime(nu)
    print("前面就是满足您输入范围的质数了")
    
main()
                
