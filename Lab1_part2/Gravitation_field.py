import turtle as t

t.shape('circle')
t.color('blue')
t.width(1)
t.speed(10)
Vx = 15
Vy = 40
dt = 0.1
ay = -10

x = -100.0
y = 0.0
T = 0.0

t.penup()
t.goto(x,y)
t.pendown()

while T < 100:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if T != 0 and y <= 0:
        Vy = 0.9 * abs(Vy)

    t.goto(x, y)
    T += 0.1


