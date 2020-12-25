# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:51:20 2020

@author: 44797
"""

def decreasing(arr, cost):
    temp = arr
    for i in range(len(temp)-1):
        if temp[i] < temp[i+1]:
            res = abs(temp[i] - temp[i+1])
            temp[i + 1] = temp[i]
            cost += decreasing(temp, cost) + res
        else:
            cost += 0
          
    return cost



def increasing(B, cost):
    for i in range(len(B)-1):
        if B[i] > B[i+1]:
            temp = abs(B[i] - B[i + 1])
            B[i + 1] = B[i]
            cost += increasing(B, cost) + temp
        else:
            cost += 0
    
    return cost
    

def sortArray(A):
    t = A.copy()
    cost = 0
    
    cost2 = decreasing(A, cost)
    
    cost1 = increasing(t, cost)
    
    
    
    # print(cost1, cost2) 
    ret = min(cost1, cost2)
    
    return ret




