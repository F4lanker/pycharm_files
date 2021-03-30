import turtle

t = turtle
n = int(input('Enter the size: '))
mult = 23
diam = 23 * n
rad = 23 * n / 2  # Радиус окружности
t.shape('turtle')
t.color('black', 'yellow')
t.begin_fill()


def rnd(size, angle=5):
    for i in range(360 // angle):
        t.left(angle)
        t.forward(size)
    t.end_fill()


def nose():
    t.pendown()
    t.right(90)
    t.width(n)
    t.color('black', 'black')
    t.forward(n * 3)
    t.penup()


def spiral():
    for i in range(90):
        t.forward(1)
        t.right(2)


rnd(n)  # Рисуем главный круг

t.penup()  # Рисуем левый глаз
t.goto(0.33 * rad, rad + 0.25 * rad)
t.pendown()
t.color('blue')
t.begin_fill()
rnd(0.12 * n)

t.penup()  # Рисуем правй глаз
t.goto(-0.33 * rad, rad + 0.25 * rad)
t.pendown()
t.begin_fill()
rnd(0.12 * n)

t.penup()  # Рисуем нос
t.goto(0, rad + 0.1 * rad)
nose()

t.goto(0.33 * rad, rad - 0.25 * rad)  # Рисуем рот
t.color('red', 'red')
t.pendown()
spiral()






