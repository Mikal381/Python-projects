# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:32:32 2022

@author: Darby Mikal Tompkins
"""

#25 checkerboard

import turtle

turtle.pensize(2)
turtle.penup()
turtle.goto(-160,-160)
turtle.pendown()
turtle.color("black")

for i in range(4):
    turtle.forward(320)
    turtle.left(90)

for y in range(-160,160,80):
    for x in range(-160,160,80):
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

        for k in range(4):
            turtle.forward(40)
            turtle.left(90)

        turtle.end_fill()       

for y in range(-120,160,80):
    for x in range(-120,160,80):
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        for k in range(4):
            turtle.forward(40)
            turtle.left(90)
        turtle.end_fill()   

turtle.done()