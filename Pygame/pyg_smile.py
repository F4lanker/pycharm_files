import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

screen.fill(white)

# здесь будут рисоваться фигуры
circle(screen, yellow, (200, 200), 150)
circle(screen, red, (140, 160), 27)
circle(screen, red, (250, 160), 27)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

