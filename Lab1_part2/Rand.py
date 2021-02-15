from random import *
import turtle as t

t.shape('turtle')
t.color('red')
t.speed(5)
while True:
    l = randint(-100, 100)
    f = randint(0, 180)
    t.forward(l)
    t.left(f)
    # x = randint(-100, 100)
    # y = randint(-100, 100)
    # t.goto(x, y)



