# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:46:30 2022

@author: Darby Mikal Tompkins
"""

lst = [
    [4,9,2],
    [3,5,7],
    [8,1,6]
]

flag_h = True
flag_v = True
flag_d = True
def magic_square(lis):
    flag_h = hori(lis)
    flag_v = vert(lis)
    flag_d = dia(lis)
   
    if flag_h == True and flag_v == True and flag_d == True:
        print ('Congratz! Your square is a magic square!!! :D ')
    else:
        print ('Sorry, not a magic square... ')
        
def hori(ls):   
    for i in ls:
        current1 = 0
        for k in i:
            current1+=k
        if flag_checkh(current1) == False:
            return False
    return True
                
def vert(ls):
    current3=0
    for key,line in enumerate(ls):
        if key == 0:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
        if key == 1:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
        if key == 2:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
    
    if flag_checkd(current3) == True:
        current3=0
        for key,line in enumerate(ls):
            if key == 0:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
            if key == 1:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
            if key == 2:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
        
        if flag_checkd(current3) == True:
            current3=0
            for key,line in enumerate(ls):
                if key == 0:
                    for each,value in enumerate(line):
                        if each == 2:
                            current3+=value
                if key == 1:
                    for each,value in enumerate(line):
                        if each == 2:
                            current3+=value
                if key == 2:
                    for each,value in enumerate(line):
                        if each == 2:
                            current3+=value
            
            return True
        else:
            return False
    else: 
        return False

def dia(ls):
    current3=0
    for key,line in enumerate(ls):
        if key == 0:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
        if key == 1:
            for each,value in enumerate(line):
                if each == 1:
                    current3+=value
        if key == 2:
            for each,value in enumerate(line):
                if each == 2:
                    current3+=value
    
    if flag_checkd(current3) == True:
        current3=0
        for key,line in enumerate(ls):
            if key == 0:
                for each,value in enumerate(line):
                    if each == 2:
                        current3+=value
            if key == 1:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
            if key == 2:
                for each,value in enumerate(line):
                    if each == 0:
                        current3+=value
        return True
        
    else:
        return False               

def flag_checkh(n):
    if n == 15:
        flag_h = True
    else:
        flag_h = False
    return flag_h
def flag_checkv(n):
    if n == 15:
        flag_v = True
    else:
        flag_v = False
    return flag_v
def flag_checkd(n):
    if n == 15:
        flag_d = True
    else:
        flag_d = False
    return flag_d

magic_square(lst)