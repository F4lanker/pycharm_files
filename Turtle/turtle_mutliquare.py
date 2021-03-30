import turtle

turtle.shape('turtle')
turtle.speed(1)
x = 40
turtle.left(90)

def multy_s(n):
    for i in range(n):
        turtle.forward(x)
        turtle.right(360 / n)
    turtle.penup()
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.pendown()
x+=60

for i in range(3, int(input('Etner the number:')) + 3):
    multy_s(i)
