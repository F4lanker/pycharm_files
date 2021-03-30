import turtle
t = turtle
t.shape('turtle')
x = 3
t.forward(x)
for i in range(40):
    x += 5
    for j in range(2):
        t.left(90)
        t.forward(x)
