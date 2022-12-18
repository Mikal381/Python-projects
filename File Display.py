# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:03:27 2022

@author: Darby Mikal Tompkins
"""

def read_numbers():
    file_object = open('numbers.txt', 'r')
    line = file_object.readline()
    line = line.rstrip('\n')
    while line != '':
        print(line)
        line = file_object.readline().rstrip('\n')
        line = line.rstrip('\n')
    file_object.close()
read_numbers()