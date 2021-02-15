import turtle as t
import math as m

t.shape('turtle')
t.speed(10)
def star(n, l):
    t.begin_fill()

    for i in range (0, n):
        t.forward(l)
        t.left(180 - 180 / n)
    t.color('orange')
    t.end_fill()
n = 17
l = 200
star(n, l)

input()
