# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:21:16 2022

@author: Darby Mikal Tompkins
"""

import random

def generate():
    lottery_list = []
    for i in range(7):
        lottery_list.append(random.randrange(0 ,10))
    print(lottery_list)
    return lottery_list
def display(lottery_list):
    for i in lottery_list:
        print(i)
lottery_list = generate()
display(lottery_list)
