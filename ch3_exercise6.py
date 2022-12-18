# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:08:48 2022

@author: Darby Mikal Tompkins
"""

#Magic Dates

month = int(input('\nEnter the month from 1 thru 12: '))
day = int(input('Enter the day from 1 thru 31: '))
year = int(input('Enter the year: '))

# 65/56/56 IS 
message = '\n' + format(month) + '/' \
            + format(day) + '/' \
            + format(year) + \
            ' IS '

if ((month * day) != year):
    message += "NOT "
    
message += "magic."

# Or this could work too
# if ((month * day) == year):
#     message += 'magic.'
# else:
#     message += 'NOT magic.'

print(message, "\n\n")