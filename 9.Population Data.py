# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:24:21 2022

@author: Darby Mikal Tompkins
"""

def main():
  counter = 0
  increaseYear = 0
  maxYear = 0
  maxYearPosition = 0
  minYear = 0
  minYearPosition = 0
  averagePeriod = 0

listNumbers = []
listNumberAverage =[]
listYears = [i for i in range(1950,1991)]

try:

    fileRead = open("USPopulation.txt", "r")

    for i in fileRead:
        counter = counter + 1

    for j in range(counter):
        listNumbers.append(0)

    fileRead.seek(0)

    for k in range(counter):
      listNumbers[k] = int(fileRead.readline())
      minYear = listNumbers[0]

    for l in range(0,counter,+1):
      
      if (l+1) == counter:
        break
  
    increaseYear = (listNumbers[l+1] - listNumbers[l])/2
  
    if increaseYear > maxYear:
        maxYear = increaseYear
        maxYearPosition = l+1
    
    if minYear > increaseYear:
        minYear = increaseYear
        minYearPosition = l+1
    

    averagePeriod = (listNumbers[counter-1] - listNumbers[0])/(counter-1)
      
    print("The average annual change in population during the time period is", '{0:,.2f}'.format(averagePeriod, ".2f"))
    print("The year with the greatest increase in population was", listYears[maxYearPosition])
    print("The year with the smallest increase in population was", listYears[minYearPosition])
    