# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:11:13 2022

@author: Darby Mikal Tompkins
"""

#hypnotic pattern

import turtle

move = 5
turtle.setheading(90)
for x in range(15):
    for y in range(4):
        turtle.forward(move)
        turtle.left(90)
        move +=5
        
import time
time.sleep(5)      