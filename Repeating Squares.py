# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:11:13 2022

@author: Darby Mikal Tompkins
"""

#Repeating Squares

import turtle

turtle.right(180)

turtle.speed(0)

length = 505

for times in range (100):
  for endtimes in range (4):
    turtle.forward(length)
    turtle.right(90)
  length -= 5  
         
        