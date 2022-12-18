# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:12:14 2022

@author: Darby Mikal Tompkins
"""

#Time Calculator

number_of_seconds = int(input("Enter number of seconds: "))
message = ""

if number_of_seconds < 0:
    message = "Enter a number above 0.\n" + \
              "Rerun program and try again."
else:
    if number_of_seconds >= 0 and number_of_seconds < 60:
        seconds = format(number_of_seconds % 60)
        message = "Seconds = " + seconds
    elif number_of_seconds >= 60 and number_of_seconds < 3600:
        minutes = format(number_of_seconds // 60)
        seconds = format(number_of_seconds % 60)
        message = "Minutes = " + minutes + \
                  " Seconds = " + seconds
    elif number_of_seconds >= 3600 and number_of_seconds < 86400:
        hours = format(number_of_seconds // 3600)
        minutes = format((number_of_seconds % 3600) // 60)
        seconds = format((number_of_seconds % 3600) % 60)
        message = "Hours = " + hours + " " + \
                  "Minutes = " + minutes + " " + \
                  "Seconds = " + seconds + " "
    elif  number_of_seconds >= 86400:
        days = format(number_of_seconds // 86400)
        hours = format((number_of_seconds % 86400) // 3600)
        minutes = format(((number_of_seconds % 86400) % 3600) // 60)
        seconds = format(((number_of_seconds % 86400) % 3600) % 60)
        message = "Days = " + days + " " + \
                  "Hours = " + hours + " " + \
                  "Minutes = " + minutes + " " + \
                  "Seconds = " + seconds + " "

print(message)