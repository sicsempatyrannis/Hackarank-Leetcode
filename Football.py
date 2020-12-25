# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:01:06 2020

@author: 44797
"""

def footballScores(A, B):
    
    a_sorted = sorted(A)
    
    ret = []
    for i in B:
        count = 0
        for j in a_sorted:
            if i >= j:
                count += 1
                
            elif j > i:
                break
        ret.append(count)
        
    return ret