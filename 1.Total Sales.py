# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:20:47 2022

@author: Darby Mikal Tompkins
"""

def calculate():
    sales = []
    total = 0
    for i in range(7):
        sale = input('Enter a store\'s sales for today: ')
        sales.append(sale)
        total += float(sale)
    print(sales)
    print(total)
calculate()
