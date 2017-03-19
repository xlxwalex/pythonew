from turtle import *
setup
colormode(255)
pensize(20)
pencolor(255,255,255)
speed(1000)
def changedraw():
    penr=254
    for i in range(100):
        circle(100,1)
        penr-=1
        pencolor((penr,penr-1,penr-2))
    for u in range(100):
        circle(-100,1)
        penr-=1
        pencolor((penr,penr-1,penr-2))
changedraw()
    
