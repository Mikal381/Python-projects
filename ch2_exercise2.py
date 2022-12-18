# -*- coding: utf-8 -*-
"""
@author: Darby Mikal Tompkins
"""

PROFIT_PERCENTAGE = .23
total_sales = float(input('\nEnter projected total sales amout: $'))
annual_profit = total_sales * PROFIT_PERCENTAGE
print('Total profit made = $' + format(annual_profit, ',.2f') + '\n')