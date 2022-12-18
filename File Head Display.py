# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:04:19 2022

@author: Darby Mikal Tompkins
"""

def read():
    file = input('Enter a file name with its extension: ')
    object_file = open(file, 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    count = 0
    while count <= 4:
        if line == '' :
            count += 5
        else:
            print(line)
            line = object_file.readline()
            line = line.rstrip('\n')
            count += 1
    object_file.close()
def main():
    read()

main()