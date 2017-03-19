#5.1
def drawsq(n):
    line=3*n+1
    for i in range(1,line+1):
        if i%3 ==1:
            print(n*"+----",end="")
            print("+")
        else:
            print  ("|    "*n,end="")
            print("|")

def main():
    n=eval(input("请输入您要的阶数："))
    drawsq(n)

main()
