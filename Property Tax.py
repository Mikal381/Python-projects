# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 22:10:11 2022

@author: Darby Mikal Tompkins
"""

#Property Tax

value = float(input('Enter the actual value of a piece of property: $'))
def assess(value):
    tax = value * 0.6 * 0.72 / 100
    print('$', format(tax, '.2f'), sep='')

assess(value)
