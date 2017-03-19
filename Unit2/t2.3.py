import turtle
 
def Snake1(rader, angle, leng):
    for i in range(leng):
        turtle.circle(rader, angle)
        turtle.circle(-rader, angle)
      
def Snake2(rader,angle, neck):
    turtle.circle(rader, angle/2)
    turtle.fd(rader)
    turtle.circle(neck + 1, 180)
    turtle.fd(rader * 2/3)
 
def main():
    turtle.setup(1200, 200, 0, 0)
    '''turtle.seth(180)
    turtle.up()
    fd(400)
    turtle.seth(0)
    turtle.pd()'''
    size = 30
    turtle.pensize(size)
    turtle.seth(-40)
    turtle.pencolor("yellow")
    Snake1(40, 80, 1)
    turtle.pencolor("black")
    Snake1(40, 80, 1)
    turtle.pencolor("pink")
    Snake1(40, 80, 1)
    turtle.pencolor("blue")
    Snake1(40, 80, 1)
    turtle.pencolor("red")
    Snake2(40, 80, size/2)
     
main()
