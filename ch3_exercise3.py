# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:08:45 2022

@author: Darby Mikal Tompkins
"""

#Age Classifier

age = int(input('Please enter a persons age.'))
if age <= 1: print('The person is an infant.')
else: print('The person is not an infant.')
if age > 1 and age > 13: print('The person is a child.')
else: print ('The person is not an infant.')
if age <= 13 and age > 20: print('The person is a teenager.')
else: print ('The person is not a teenager.')
if age >=20: print ('The person is an adult.')
