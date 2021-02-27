# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:13:37 2020

@author: 44797
"""

def selectStock(saving, currentValue, futureValue):
    mem = {}
    for i, j in enumerate(currentValue):
        mem[j] = futureValue[i] - j
    
    global_max = 0
    print(mem)
    for i in currentValue:
        bank = saving
        seen = []
        bank -= i
        stack = sorted([j for j in currentValue if j <= bank and j != i])
        stack_1 = []
        temp_max = mem[i]
        
        while stack:
            top = stack.pop()

            if top > bank and top not in seen:
                add = stack_1.pop()
                bank += add
                temp_max -= mem[add]
                stack.append(top)
                
            else:
                bank -= top
                seen.append(top)
                stack_1.append(top)
                temp_max += mem[top]
        
        global_max = max(global_max, temp_max)
        
    return global_max
                
            
        
                
            
            
            
print(selectStock(1000, [175,133,109,210,235,673,56,34,76,890], [200,125,128,228,152,300,200,545,44,620]))
            
    
   

    
    
    