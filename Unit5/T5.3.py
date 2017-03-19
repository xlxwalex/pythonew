#5.3
def isALL(n):
    if type(n)==type(1) or type(n)==type(1.2) or type(n)==type(4j):
        print("True")
    else:
        print("False")

try:
    strn=eval(input("请输入您的数据："))
    isALL(strn)
except:
    print("False")
