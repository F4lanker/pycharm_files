import turtle

turtle.shape('turtle')
turtle.speed(30)


def cycle():

    for i in range(120):
        turtle.forward(2)
        turtle.left(3)
    turtle.right(60)


for i in range(6):
    cycle()
