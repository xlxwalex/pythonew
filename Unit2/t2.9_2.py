from turtle import *
from random import randint
setup
colormode(255)
pensize(20)
pencolor(255,255,255)
speed(1000)
penup()
setpos(-100,-100)
down()
penr,peng,penb=0,0,0
def changedraw():
    penr=254
    for i in range(100):
        circle(100,1)
        penr,peng,penb = randint(0,255),randint(0,255),randint(0,255)
        pencolor((penr,peng,penb))
    for u in range(100):
        circle(-100,1)
        penr,peng,penb = randint(0,255),randint(0,255),randint(0,255)
        pencolor((penr,peng,penb))
changedraw()
    
