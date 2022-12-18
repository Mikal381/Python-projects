# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:12:47 2022

@author: Darby Mikal Tompkins
"""

# Wi-Fi Dignostic Tree

print("Reboot the computer and try to connect.\n(Y/N) Enter Y for yes or N for no.")

user_answer = input("Did that fix the problem? ")

if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
    if user_answer == "n" or user_answer == "N":
        print("Reboot the router and try to connect.")
        user_answer = input("Did that fix the problem? ")

        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
            if user_answer == "n" or user_answer == "N":
                print(" Make sure the cables \nbetween the router & modem\nare plugged in firmly.")
                user_answer = input("Did that fix the problem? ")

                if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                    if user_answer == "n" or user_answer == "N":
                        print("Move the router to\nto a new location\nand try to connect")
                        user_answer = input("Did that fix the problem? ")

                        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                            print("Get a new router")
                        else:
                            print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
                else:
                    print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
        else:
            print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
else:
    print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
