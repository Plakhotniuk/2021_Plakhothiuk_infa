from random import randint
import turtle


number_of_turtles = 30
steps_of_time_number = 50
turtle.speed(10)
turtle.penup()
turtle.shape('circle')
turtle.goto(-200, -200)
turtle.pendown()
for i in range(4):
    turtle.forward(400)
    turtle.left(90)
turtle.hideturtle()
turtle.penup()

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    f = randint(0, 360)
    unit.left(f)



for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)
        if abs(unit.xcor()) > 200 or abs(unit.ycor()) > 200:
            if unit.xcor() > 0:
                f = unit.towards(200, 0)
                unit.left(2 * f)
                unit.forward(3)
            if unit.xcor() < 0:
                f = unit.towards(200, 0)
                unit.right(2 * f)
                unit.forward(3)


input()
