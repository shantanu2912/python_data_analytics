from turtle import *
pencolor('red')
pensize(8)
speed('fastest')
bgcolor('black')
n = 0 
while n <= 200:
    fd(100+n)
    rt(360/6)
    write(n, font=('Calibri', 15))
    n+=5
hideturtle()
mainloop()