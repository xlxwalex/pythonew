#4.6 by肖老师
import random

times = eval(input("请输入你希望模拟的次数："))

pick_first_n = 0
pick_change_n = 0

for i in range(times):
    car = random.randint(0, 2)  #生成哪个门后藏车
    pick_first = random.randint(0, 2)    #初始随机选一个
    if pick_first == car:   #如果直接选中，则初始选择正确，pick_first_n 加 1，换选择一定不中
        pick_first_n += 1
    else:                   #如果初始选择没中，则主持人打开另一扇没车的门后，换选择一定中
        pick_change_n += 1  #故 pick_change_n 加 1

pick_first_percent = pick_first_n / times       #计算坚持不换选择的胜率
pick_change_percent = pick_change_n / times     #计算换选择的胜率
print("如果坚持初选，胜率为{:.2f}%".format(pick_first_percent * 100))
print("如果改变初选，胜率为{:.2f}%".format(pick_change_percent * 100))
