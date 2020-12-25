# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:55:13 2020

@author: 44797
"""

import sys

def maxMultiple(A):
    max_multiple = -sys.maxsize
    for i in A:
        if i%3 == 0 and i > max_multiple and (i >= 3 or i <= -3):
            max_multiple = i
            
            
    return max_multiple
            

