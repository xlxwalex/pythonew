#3.4
while 1:
    hui=input("请输入一个五位数或用e退出：")
    if len(hui) == 5 :
        if eval(hui)==eval(hui[-1:]+hui[3:4]+hui[2:3]+hui[1:2]+hui[0:1]):
            print("这是一个回文数")
        else:
            print("这不是一个回文数")
    elif hui[-1:] in ['e','E']:
        break
    else:
        print("您的输入有误")
    
    
