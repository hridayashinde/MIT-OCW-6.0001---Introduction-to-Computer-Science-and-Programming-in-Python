# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:32:13 2020

@author: hridaya
"""
    
annual_salary=float(input("Enter your annual salary: "))
total_cost=1000000
portion_down_payment=0.25*total_cost

current_savings=float(0)
months=int(0)
epsilon=100
low=0
high=100
mid=(low+high)/2
num_guess=0
loop=0
def calc_current_saving(salary,r):
    
    investment=float(0)
    savings=float(0)
    for i in range(36):
        if i%6==0 and i>0:
            salary=salary+(salary*0.07)
        
        investment=savings*0.04/12
        savings=savings+investment+(salary*r/1200)
        
    return savings

while abs(current_savings-portion_down_payment)>=epsilon and loop==0:
    mid=(low+high)/2
    
    current_savings=calc_current_saving(annual_salary,mid)
    
    
    if current_savings<portion_down_payment:
        low=mid
        
    else :
        high=mid
    
    if mid==100:
        loop=loop+1
    
    
        
    
        
    num_guess +=1
   
    

if abs(current_savings-portion_down_payment)<=epsilon:
    print("best saving rate:",mid/100)
    print("number of tries:",num_guess)
else:
    print("sorry it is not possible to pay down payment in 3 years")
    







