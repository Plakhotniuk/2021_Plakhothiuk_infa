# EX 4
# import turtle as t
# import math as m
#
# t.shape('turtle')
#
# n = 1
# R = 30
# n1 = 50
# L = 2 * R * m.sin(m.pi/n1)
#
# while n < 360:
#     t.forward(L)
#     t.left(360 / n1)
#     n += 360 / n1
#
# input()

# EX 5
# import turtle
#
# turtle.shape('turtle')
#
#
# def turn(m, d):
#     turtle.forward(m)
#     turtle.left(90)
#     turtle.forward(m)
#     turtle.left(90)
#     turtle.forward(m)
#     turtle.left(90)
#     turtle.forward(m)
#     turtle.left(90)
#     turtle.penup()
#     turtle.goto(-d, -d)
#     turtle.pendown()
#
# d = 10
# l = 2 * d
# for i in range(0, 10, 1):
#     turn(l, d)
#     d += 10
#     l = 2 * d
#
#
# input()

# EX 6
# import turtle as t
#
# t.shape('turtle')
# n = int(input())
# for i in range(0, n, 1):
#     t.forward(100)
#     t.stamp()
#     t.left(180)
#     t.forward(100)
#     t.left(180 - 360//n)
# input()

# import turtle as t
# import math as m
#
# t.shape('turtle')
#
# n = 1
# R = 1
# n1 = 50
# a = 5
#
# while n < 360:
#     L = 2 * R * m.sin(m.pi / n1)
#     R *= 5 /(2 * m.pi) * 180 / m.pi
#
#     t.forward(L)
#     t.left(360 / n1)
#     n += 360 / n1
#
# input()
# print(L)
# EX 7
# import turtle as t
# import math
#
# t.shape('turtle')
# n = 1
# while n < 360:
#     t.forward(5 / (2 * 360) * n * math.sqrt(1 + 4 * 3.14 ** 2))
#     t.left(5)
#     n += 1
#
# input()



# EX 8
# import turtle as t
#
# t.shape('turtle')
#
# def turn(m):
#     t.forward(m)
#     t.left(90)
#
# d = 2
# l = 2 * d
# for i in range(0, 40, 1):
#     turn(l)
#     d += 2
#     l = 2 * d
#
# input()
