# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:08:32 2022

@author: Darby Mikal Tompkins
"""

# Celsius to Fahrenheit Table

print('Celsius\t', 'Fahrenheit')
print('-' * 20)
for c in range(21):
    print(format(c, '2.0f'), '\t', format(9 / 5 * c + 32, '.2f'))
    
