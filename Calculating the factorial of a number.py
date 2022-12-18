# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:08:56 2022

@author: Darby Mikal Tompkins
"""

# Calculating the factorial of a number

number = int(input("enter the number: "))
factorial = 1

for x in range(1, number+1):
    factorial *= x
    print("the factorial of ",number,"is", factorial) 
    