# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:11:17 2021

@author: 44797
"""

def starsBars(string, start, end):
    ret = []
    
    for i in range(len(start)):
        start_ind = start[i] - 1
        end_ind = end[i]
        slice_string = string[start_ind:end_ind]
        
        star_count = 0
        bar_count = 0
        temp_count = []
        if slice_string.count('|') >= 2 and '*' in slice_string:
            for j in slice_string:
                if ord(j) == 124:
                    bar_count += 1
                    if bar_count == 2:
                        bar_count -= 1
                        temp_count.append(star_count)
                        star_count = 0   
                
                elif j == '*' and bar_count >= 1:
                    star_count += 1
                
            ret.append(sum(temp_count))
            
        else:
            ret.append(0)
        
      
    return ret
                    
    

print(starsBars('*|*|', [1], [3]))

