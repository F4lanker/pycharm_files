import turtle

turtle.shape('turtle')
x = 50
for i in range(2):
    for j in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.penup()
    turtle.right(120)
    turtle.forward(5)
    turtle.pendown()
    x += 15
