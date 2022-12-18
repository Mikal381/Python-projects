# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:33:08 2022

@author: Darby Mikal Tompkins
"""

#How much is insurance?

cost = float(input('Enter the replacement cost of a building: $'))
def calculate(cost):
    insurance = cost * 0.8
    print('The minimum amount of insurance you should buy for the property is $', format(insurance, '.2f'))

calculate(cost)