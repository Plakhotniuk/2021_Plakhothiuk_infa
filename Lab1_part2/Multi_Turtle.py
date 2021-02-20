from random import randint
import turtle
import math


number_of_turtles = 10
steps_of_time_number = 100
turtle.speed(10)
turtle.penup()
turtle.shape('circle')
turtle.goto(-200, -200)
turtle.pendown()
size_of_pool = 400
for i in range(4):
    turtle.forward(size_of_pool)
    turtle.left(90)
turtle.hideturtle()
turtle.penup()

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
coord = [[1., 1.]]
velocity = [[1., 1.]]
i = 0


for unit in pool:
    unit.penup()
    unit.speed(50)
    coord.append([randint(-200, 200), randint(-200, 200)])
    velocity.append([randint(-5, 5), randint(-5, 5)])
    unit.goto(coord[i])
    i += 1
    unit.left(randint(0, 360))


for j in range(steps_of_time_number):
    for i in range(number_of_turtles):
        coord[i][0] += velocity[i][0]
        coord[i][1] += velocity[i][1]

        if abs(coord[i][0]) > size_of_pool//2:
            velocity[i][0] = -1 * velocity[i][0]
        if abs(coord[i][1]) > size_of_pool//2:
            velocity[i][1] = -1 * velocity[i][1]

        pool[i].goto(coord[i][0], coord[i][1])
input()