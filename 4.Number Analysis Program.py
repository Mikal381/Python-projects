# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:22:55 2022

@author: Darby Mikal Tompkins
"""

numbers = []
total = 0
for i in range(20):
    number = int(input('Enter a number as a integer: '))
    numbers.append(number)
    total += number
print('The lowest number in the list is', min(numbers))
print('The highest number in the list is', max(numbers))
print('The total in the list is', total)
print('The average in the list is', total / 20)
