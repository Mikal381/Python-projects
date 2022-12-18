# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:11:57 2022

@author: Darby Mikal Tompkins
"""

#Software Sales

PRICE_PER_PACKAGE = 99.00

number_of_packages = float(input('\nEnter # of packages purchased: '))

display_message = ""

if number_of_packages < 0:
    display_message = "Error. # of packages must be greater than 0.\nRe-run program and try again."
else:
    discount_percentage = 0

    if number_of_packages < 10:
        discount_percentage = 0
    elif number_of_packages >= 10 and number_of_packages <= 19:
        discount_percentage = .10 # 10%
    elif number_of_packages >= 20 and number_of_packages <= 49:
        discount_percentage = .20 # 20%
    elif number_of_packages >= 50 and number_of_packages <= 99:
        discount_percentage = .30
    elif number_of_packages >= 100:
        discount_percentage = .40 # 40%
    
    package_total = number_of_packages * PRICE_PER_PACKAGE
    discount_amount = (package_total) * discount_percentage
    grand_total = package_total - discount_amount
    display_message = "Package total = $" + format(package_total, ',.2f') + \
                      "\nDiscount Percentage = " + format(discount_percentage, '.0%') + \
                      "\nDiscount amount = $" + format(discount_amount, ',.2f') + \
                      "\nGrand total  = $" + format(grand_total, ',.2f')


print("\n" + display_message + "\n")