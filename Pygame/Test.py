import pygame
from pygame.draw import *
import colors as cl

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 50
y = 50
width = 40
height = 60
speed = 5
isJump = False
Jumpcount = 10

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if keys[pygame.K_UP] and y >= 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        y += speed
    if keys[pygame.K_SPACE]:
        isJump is True

    win.fill(cl.black)
    rect(win, cl.blue, (x, y, width, height))
    pygame.display.update()


pygame.quit()