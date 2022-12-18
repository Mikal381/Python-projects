# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:04:50 2022

@author: Darby Mikal Tompkins
"""

def count():
    object_file = open('names.txt', 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    count = 0
    while line != '':
        count += 1
        line = object_file.readline()
        line = line.rstrip('\n')
    object_file.close()
count()
print()
