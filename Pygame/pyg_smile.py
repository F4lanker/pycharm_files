import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

def circ(color, coordinat, radius):
    circle(screen, color, coordinat, radius)  # main circle
    circle(screen, black, coordinat, radius, 1)

screen.fill(white)

# здесь будут рисоваться фигуры
circ(yellow, (200, 200), 150)  # Face frame
circ(red, (140, 160), 30)  # Left eye frame
circ(red, (250, 160), 26)  # Right eye frame
circ(black, (140, 160), 14)  # Eye center left
circ(black, (250, 160), 12)  # Eye center right
rect(screen, black, (150, 250, 100, 36))  # Mouth
rect(screen, red, (100, 220, 150, 25), 0, -28, -30)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

