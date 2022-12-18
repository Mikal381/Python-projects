# -*- coding: utf-8 -*-
"""
@author: Darby Mikal Tompkins
"""

charge_for_food = float(input('\nEnter charge for food: $'))
TIP_PERCENTAGE =0.18
SALES_TAX =0.07
tip = (charge_for_food * TIP_PERCENTAGE)
sales_tax = (charge_for_food * SALES_TAX)
grand_total = charge_for_food + tip + sales_tax
print('\nCharge for food = $', format(charge_for_food, ',.2f'), sep='')
print('Tip = $', format(tip, ',.2f'), sep='')
print('Sales tax = $', format(sales_tax, ',.2f'), sep='')
print('Grand total = $', format(grand_total, ',.2f'), sep='', end='\n\n')
