#4.3
a,b=eval(input("请输入两个整数，中间用,隔开："))
c=a*b
if a<b:
    a,b=b,a
while False == (a in[0,1]):
     b,a=a,b%a
c=c/b
print("最小公约数为：{},最大公倍数为：{}".format(b,c))

    
