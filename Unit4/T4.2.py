#4.2
stri=input("请输入您想要的字符串：")
kong=0
alpha=0
chi=0
num=0
other=0
for i in stri:
    if i == " ":
        kong +=1
    elif '0' <= i <= '9':
        num+=1
    elif i>=u'\u4e00' and i<=u'\u9fa5':
        chi+=1
    elif True == i.isalpha():
        alpha+=1
    else:
        other+=1
print("您输入的字符串中有{}个空格,{}个数字,{}个中文,{}个英文字符,{}个其他字符".format(kong,num,chi,alpha,other))
