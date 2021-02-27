# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:11:17 2021

@author: 44797
"""

def starsBars(string, start, end):
    ret = []
    dp = {}
    
    if '*' not in string or '|' not in string:
        return [0] * len(start)
    for i in range(len(start)):
        start_ind = int(start[i]) - 1
        end_ind = int(end[i])
        slice_string = string[start_ind:end_ind]
        
    
        
        if (start_ind, end_ind) in dp.keys():
            ret.append(dp[(start_ind, end_ind)])
                
        elif slice_string.count('|') >= 2 and '*' in slice_string and (start_ind, end_ind) not in dp.keys():
            left_ind = slice_string.find('|')
            right_ind = slice_string.rfind('|')
            new_string = slice_string[left_ind:right_ind]
        
            dp[(start_ind, end_ind)] = new_string.count('*')
            ret.append(dp[(start_ind, end_ind)])
            
        elif (start_ind, end_ind) not in dp.keys():
            dp[(start_ind, end_ind)] = 0  
            ret.append(dp[(start_ind, end_ind)])
        
  
    return ret
                    
    
with open('end_index.txt', 'r') as f:
    end_index = [line.strip() for line in f]

with open('start_index.txt', 'r') as f:
    start_index = [line.strip() for line in f]
    
with open('output002.txt', 'r') as f:
    expected = [line.strip() for line in f]
    

myout = starsBars('|||||******|**|****|******|*|*||*|******|*||**|***|***|**||*|**|***|*|*|**||***|******|*|||*****||||', start_index, end_index)
print(len(myout), len(expected))
print(start_index[39], end_index[39], expected[39], myout[39])

        
