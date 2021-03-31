'''
the programm print post index standart digits inputed by user
'''

# imports
from math import sqrt
from turtle import *

shape('turtle')
width (3)
font_high = 50
font_width = 25
hypotenuza = sqrt((font_high/2)**2 + font_width**2)
gap = 12
index = list(map(int, input('Enter 6 digits of index without spaces and press Enter: ')))

def main():  # The main function define which figure turtle print
    for i in index:
        if i == 0:
            zero()
        elif i ==1:
            one()
        elif i == 2:
            two()
        elif i == 3:
            three()
        elif i == 4:
            four()
        elif i == 5:
            five()
        elif i ==6:
            six()
        elif i == 7:
            seven()
        elif i == 8:
            eight()
        elif i == 9:
            nine()

def even(num):  # The function returns width for even i and high for not even
    if num % 2 == 0:
        return font_width
    else:
        return font_high


def zero():
    pendown()
    for i in range(4):
        forward(even(i))
        left(90)
    penup()
    forward(gap + font_width)
    pendown()


def one():
    penup()
    left(90)
    forward(font_high/2)
    pendown()
    right(45)
    forward(hypotenuza)
    right(135)
    forward(font_high)
    penup()
    left(90)
    forward(gap)


def two():
    penup()
    left(90)
    forward(font_high)
    pendown()
    right(90)
    forward(font_width)
    right(90)
    forward(font_high/2)
    right(45)
    forward(hypotenuza)
    left(135)
    forward(font_width)
    penup()
    forward(gap)


def three():
    penup()
    left(90)
    forward(font_high)
    pendown()
    right(90)
    forward(font_width)
    right(135)
    forward(hypotenuza)
    left(135)
    forward(font_width)
    right(135)
    forward(hypotenuza)
    left(135)
    penup()
    forward(font_width + gap)

def four():
    penup()
    left(90)
    forward(font_high)
    pendown()
    right(180)
    forward(font_high/2)
    left(90)
    forward(font_width)
    left(90)
    forward(font_high/2)
    right(180)
    forward(font_high)
    penup()
    left(90)
    forward(gap)


def five():
    penup()
    forward(font_width)
    left(90)
    forward(font_high)
    pendown()

def six():
    pass


def seven():
    pass

def eight():
    pass

def nine():
    pass

main()





