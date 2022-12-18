# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:11:39 2022

@author: Darby Mikal Tompkins
"""

#Money Counting Game

PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25

pennies = float(input("Enter number of pennies: "))
nickels = float(input("Enter number of nickels: "))
dimes = float(input("Enter number of dimes: "))
quarters = float(input("Enter number of quarters: "))

pennies *= PENNY # pennies = pennies * PENNY
nickels *= NICKEL
dimes *= DIME
quarters *= QUARTER

total = pennies + nickels + dimes + quarters

message = ""

if total == 1.00:
    message = "You Won! The amount entered equals 1 dollar."
else:
    message = "You Lost! "

    if total > 1.00:
        message += "The amount entered is greater than 1 dollar."
    else:
        message += "The amount entered is less than 1 dollar."

print(message)