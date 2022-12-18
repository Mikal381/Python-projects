# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:05:37 2022

@author: Darby Mikal Tompkins
"""

def write():
    member = int(input('Enter the number of member: '))
    object_file = open('golf.txt', 'w')
    for i in range(member):
        name = input('Enter a player\'s name: ')
        score = input('Enter his or her score: ')
        object_file.write(name + '\n')
        object_file.write(score + '\n')
    object_file.close()
    return object_file
def read():
    object_file = open('golf.txt', 'r')
    for i in object_file:
        i = i.rstrip('\n')
        print(i)
write()
read()

