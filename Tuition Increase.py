# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:08:53 2022

@author: Darby Mikal Tompkins
"""

# Tuition Increase

tuition = 8000
print("Year \tTuition")
for x in range(1,6):
    tuition += tuition*0.03
    print(x, "\t\t$", format(tuition, '.2f'))