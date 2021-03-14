# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:55:54 2021

@author: 44797
"""
from collections import Counter
import collections
class Solution:
    def frequencySort(self, nums):
        nums_count = collections.OrderedDict(sorted(Counter(nums).items(), key=lambda x: x[0], reverse=True))
        output = []
        sorted_count = dict(sorted(nums_count.items(), key=lambda x: x[1]))
        
        for i in sorted_count:
            for _ in range(nums_count[i]):
                output.append(i)
                
        return output
    
nums = [1,1,2,2,2,3]
sol = Solution().frequencySort(nums)
print(sol)