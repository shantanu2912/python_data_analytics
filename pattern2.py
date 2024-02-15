from turtle import *
speed(0)

def polygon(side,size):
    for i in range(side):
        forward(size)
        left(360/side)
polygon(7,100)
hideturtle()
mainloop()