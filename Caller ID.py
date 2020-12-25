# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:45:18 2020

@author: 44797
"""

def callID(phone_numbers, phone_owners, number):
    
    
    for i, j in enumerate(phone_numbers):
        if j == number:
            return phone_owners[i]
        
    return number
        
 