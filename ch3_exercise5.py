# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:08:48 2022

@author: Darby Mikal Tompkins
"""

#Mass and Weight

mass = float(input('Enter an object\'s mass: '))

weight = mass * 9.8

message = "\nThe object"

if weight < 100:
    message += ' is too light at ' + format(weight, ',.2f') + ' newtons.'
elif weight >= 100 and weight <= 500:
    message += '\'s weight at ' + format(weight, ',.2f') + ' is just right.'
elif weight > 500:
    message += ' is too heavy at ' + format(weight, ',.2f') + ' newtons.'

print(message, end="\n\n")