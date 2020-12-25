# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:08:15 2020

@author: 44797
"""


    
    
def kickStart(s):
    a = 'KICK'
    b = 'START'
    
    count = 0
    
    for i in range(len(s)-len(a)):
        if s[i:i+len(a)] == a:
            for j in range(i+len(a), len(s)):
                if s[j:j+len(b)] == b:
                    count += 1
                    
    return count
                

T = int(input())

for i in range(1, T+1):
    s = str(input())
    print('Case #{}: '.format(i), kickStart(s))