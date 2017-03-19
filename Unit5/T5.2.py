#5.2
def isOdd(n):
    if num%2==0:
        return False
    else:
        return True
    
try:
    num=eval(input("请输入一个整数："))
    if type(num)==type(1):
        print("这是一个奇数.") if isOdd(num) == True else print("这不是一个奇数.")
    else:
        print("您输入的不是整数")
except:
    print("您输入的不是整数")
    
