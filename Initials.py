# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 02:14:09 2022

@author: Darby Mikal Tompkins
"""

# 01. Initials
def get_name():
    first = input('Enter your first name: ')
    middle = input('Enter your middle name: ')
    last = input('Enter your last name: ')
    print(first[0].upper(), '.', middle[0].upper(), '.', last[0].upper(), '.', sep='')
get_name()
