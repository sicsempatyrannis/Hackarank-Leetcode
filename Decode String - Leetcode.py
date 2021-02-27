# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:24:52 2021

@author: 44797
"""

#Open bracket tracking.
import re

class Solution():
    def repeated_element(self, substring):
        
        opened = 1
        
        for i, j in enumerate(substring):
            if j == '[':
                opened += 1
           
            elif j == ']':
                opened -= 1
                if opened == 0:
                    curr_index = i
                    
                    return substring[:curr_index]
                    
    def decodeString(self, s: str) -> str:
        ind = re.search(r"\d", s)
        if not ind:
            return s
        
        ind = ind.start()
        char = s[ind]
        extension = 0
        
        
        if s[ind:ind+2].isdigit():
            char = s[ind:ind+2]
            extension = 1
            
        if s[ind:ind+3].isdigit():
            char = s[ind:ind+3]
            extension = 2
            
        start_index = ind+extension
        string_to_decode = self.repeated_element(s[start_index+2:])
        to_be_replaced = char + '[' + string_to_decode + ']'
        decoded = s.replace(to_be_replaced, string_to_decode*int(char)) 

        
        if decoded.isalpha():
            return decoded
        else:
            return self.decodeString(decoded)
        
                
obj = Solution()
result = obj.decodeString("100[leetcode]")
print(result)

                           