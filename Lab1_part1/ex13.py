import turtle as t
import math as m

t.shape('turtle')



def draw1(r, col):
    n = 1
    L = 2 * r * m.sin(m.pi/n1)

    t.pendown()

    t.begin_fill()

    while n < 360:
        t.forward(L)
        t.left(360 / n1)
        n += 360 / n1
    t.color(col)
    t.end_fill()
    t.penup()

def draw2(r, col):
    n = 1
    L = 2 * r * m.sin(m.pi/n1)

    t.pendown()

    t.color(col)

    while n < 180:
        t.forward(L)
        t.right(360 / n1)
        n += 360 / n1


    t.penup()
t.speed(50)
R = 100
n1 = 100
r = 20
r1 = 40
draw1(R, 'yellow')
t.color('black')
t.goto(-50, 120)
draw1(r, 'blue')
t.goto(50, 120)
t.color('black')
draw1(r, 'blue')

t.goto(3, 100)
t.right(90)
t.pendown()
t.color('black')
t.width(10)
t.forward(30)
t.penup()
t.goto(45, 70)
draw2(r1, 'red')




input()