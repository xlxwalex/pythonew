#5.7
nt=eval(input("请输入您所需的汉诺塔阶数："))
def move(nt,a,b,c):
    if nt==1:
        print(a,"->",c)
        return
    move(nt-1,a,c,b)
    move(1,a,b,c)
    move(nt-1,b,a,c)
move(nt,"a","b","c")
