# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:05:11 2022

@author: Darby Mikal Tompkins
"""

def count():
    object_file = open('numbers.txt', 'r')
    total = 0
    for i in object_file:
        i = int(i.rstrip('\n'))
        total += i
        print(i)
    print('The total is', total)
    object_file.close()
count()
