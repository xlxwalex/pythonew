#3.3
contin=10
skill=1
uper=0
ti=0
skit=1
for i in range(1,365):
     ti+=1
     if 4<=ti<=7:
         uper+=0.01
     if i % contin == 0 :
         uper=0
         ti=0
         skit=skill
     skill*=(1+uper)
print("工作{}，休息一天的方式，365天后的能力值为：{:.2f}".format(contin,skill))
         
         
        
