# EX 9
# import turtle
# import math as m
# turtle.shape('turtle')
# def move(n, l):
#     for i in range(3, n, 1):
#         turtle.left(90 * (i-2)/ i)
#         for j in range(i, 0, -1):
#             turtle.left(360 / i)
#             turtle.forward(l)
#
#
#         turtle.right(90 * (i-2)/ i)
#         turtle.penup()
#
#         turtle.forward(abs((l + 10)/(2 * m.sin(m.pi / (i + 1))) - l/(2 * m.sin(m.pi / (i)))))
#         turtle.pendown()
#         l += 10
#
# move(10, 50)
#
# input()


# EX 10
#
# import turtle as t
#
# t.shape('turtle')
#
#
# def eight(l):
#     n = 0
#     k = 5
#     while n <= 360:
#         t.forward(l)
#         t.left(k)
#         n+=k
#     p = 0
#     while p <= 360:
#         t.forward(l)
#         t.right(k)
#         p+=k
#
#
# a = 10
#
# n = 10
#
# for i in range(0, n, 1):
#     eight(a)
#     t.left(360 / n)
#


# EX 11
#
# import turtle as t
#
# t.shape('turtle')
#
#
# def eight(l):
#     n = 0
#     k = 10
#     while n < 360:
#         t.forward(l)
#         t.left(k)
#         n+=k
#     p = 0
#     while p < 360:
#         t.forward(l)
#         t.right(k)
#         p+=k
#
#
# a = 10
#
# n = 10
#
# for i in range(0, n, 1):
#     eight(a)
#     a += 5
#

