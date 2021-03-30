import turtle

turtle.shape('turtle')
turtle.speed(50)
turtle.left(90)

def cycle(angle, length):
    for i in range(360//angle):
        turtle.left(length)
        turtle.forward(angle)
    turtle.right(180)


for i in range(1, 3):
    cycle((i+2), (i+6))

