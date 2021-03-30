import turtle
import random

t = turtle
t.shape('turtle')
t.color('red')
for i in range(int(input('How much move you want - '))):
     if random.randint(1, 150) % 2 == 0:
         t.right(random.randint(0, 180))
         t.forward(random.randint(1, 50))
     else:
         t.left(random.randint(0, 180))
         t.forward(random.randint(1, 80))