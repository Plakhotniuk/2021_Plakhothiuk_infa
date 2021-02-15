import turtle as t

t.shape('turtle')
t.color('blue')
t.width(5)
t.speed(5)
t.left(90)
One = (100, 135, 60, 180, 60, 225, 100, 90)
Four = (100, 180, 50, 270, 50, 270, 50, 180, 50,  90, 50, 270, 50, 90)
Zero = (100, 90, 50, 90, 100, 90, 50)
Seven = (50, 315, 70, 135, 50, 180, 50, 225, 70, 45, 50, 90)

n = int(input())

a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 1:
        a[i] = One
    if a[i] == 4:
        a[i] = Four
    if a[i] == 7:
        a[i] = Seven
    if a[i] == 0:
        a[i] = Zero
# print(a)
for i in a:
    t.pendown()
    if i == Seven:
        t.penup()
        t.left(90)
        t.forward(40)
        t.right(90)
        t.pendown()
    for k, j in enumerate(i):
        if k % 2 == 0:
            t.forward(j)
        else:
            t.left(j)
    t.penup()
    if i == Seven:
        t.forward(110)
        t.left(90)
    else:
        t.forward(70)
        t.left(90)

input()



