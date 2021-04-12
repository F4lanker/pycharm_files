import pygame
from pygame.draw import *

pygame.init()
pygame.display.set_caption('Angry smile')
FPS = 30
screen = pygame.display.set_mode((400, 400))
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
x = 200
y = 200
speed = 5

def circ(color, coordinat, radius):
    circle(screen, color, coordinat, radius)  # main circle
    circle(screen, black, coordinat, radius, 1)


#def brow(start_pos, end_pos):
    #line(screen, black, start_pos, end_pos)


screen.fill(white)

# здесь будут рисоваться фигуры
circ(yellow, (200, 200), 150)  # Face frame
circ(red, (140, 160), 30)  # Left eye frame
circ(red, (250, 160), 26)  # Right eye frame
circ(black, (140, 160), 14)  # Eye center left
circ(black, (250, 160), 12)  # Eye center right
rect(screen, black, (150, 250, 100, 36))  # Mouth
#brow(120, 250)

rect(screen, red, (100, 220, 150, 25), 0, -28, -30)



finished = False

while not finished:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_SPACE]:
        print('Cuurent X:', x, 'Current Y:', y)

    circle(screen, black, (x, y), 2)
    pygame.display.update()


pygame.quit()