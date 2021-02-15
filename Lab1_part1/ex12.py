import turtle as t
import math as m

t.shape('turtle')



def sp(R,r):

    N = 30

    L = 2 * R * m.sin(m.pi/N)

    l = 2 * r * m.sin(m.pi / N)

    n = 0

    while n < 180:
        t.forward(L)
        t.right(360 / N)
        n += 360 / N
    p = 0
    while p < 180:
        t.forward(l)
        t.right(360 / N)
        p += 360 / N

R = 30
r = 5

t.left(90)
for i in range (10):
    sp(R, r)

input()



