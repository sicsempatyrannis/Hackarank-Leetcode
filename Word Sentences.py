# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:07:53 2020

@author: 44797
"""

def anagramSentence(wordset, sentence):
    ret = []
    for i, j in enumerate(sentence):
        
        sent_list = j.split()
        res = 1
        for a, b in enumerate(sent_list):
            count = 0
            for m, n in enumerate(wordset):
                if sorted(n) == sorted(b) and n != b:
                    count += 1
                
            res *= count  
        ret.append(res)
                
    return ret
                    
    