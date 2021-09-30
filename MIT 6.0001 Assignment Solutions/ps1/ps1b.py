# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:21:38 2020

@author: hridaya
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:59:13 2020

@author: dhruv
"""
annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home:​ "))
portion_down_payment=0.25*total_cost
semi_annual_raise=float(input("The semi­annual salary raise:"))
current_savings=float(0)
r=0.04
months=int(0)



while current_savings<portion_down_payment:
    if months%6==0 and months>0:
        annual_salary=annual_salary+(annual_salary* semi_annual_raise)
    
    monthly_investment=current_savings*r/12
    current_savings=current_savings + monthly_investment+(annual_salary*portion_saved/12)
    months +=1


print("Number of months:",months)
    
    
    