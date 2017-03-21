#T2.2
try:
    while 1:
        money=input("请输入要转换的金额，例子：$2/￥6的形式,e退出：")
        mode=money[0]
        if mode == '$':
            val=eval(money[1:])
            trans=val*6
            print('{}->>￥{}'.format(money,trans))
        elif mode == '￥':
            val=eval(money[1:])
            trans=val/6
            print('{}->>${}'.format(money,trans))
        elif mode =='e':
            break
        else:
            print("您输入的有误")
except:
    print("您输入的有误")
