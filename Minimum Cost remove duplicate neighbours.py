# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:28:31 2020

@author: 44797
"""

def solution(S, C):
    # write your code in Python 3.6
    res = 0
    in_streak, streak_max, streak_total = False, 0, 0
    
    S += '#'
    
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            in_streak = True
            streak_max = max(C[i], streak_max)
            streak_total += C[i]
            
        elif in_streak:
            in_streak = False
            res += streak_total + C[i] - max(C[i], streak_max)
            streak_total, streak_max = 0, 0
            
    return res
    