# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:12:11 2022

@author: Darby Mikal Tompkins
"""

#Body Mass Index

weight = float(input("Enter weight (in pounds): "))
height = float(input("Enter height (in inches): "))
message = "Your weight is considered "

BMI = (weight * (703 / (height**2)))

if BMI >= 18.5 and BMI <= 25:
    message += "optimal weight"
elif BMI < 18.5:
    message += "underweight"
elif BMI > 25:
    message += "overweight"

message += " @ BMI = " + format(BMI, ',.2f')

print(message4