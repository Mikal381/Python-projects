# -*- coding: utf-8 -*-
"""
@author: Darby Mikal Tompkins
"""

R = float(input('Enter the length of the row, in feet: '))
E = float(input('Enter amount of space used by an end-post assembly: '))
S = float(input('Enter amount of space between vines: '))
V = (R - (2 * E)) / S
print('Number of grapevines that will fit in a row = ', V)