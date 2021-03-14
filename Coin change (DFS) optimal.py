# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:34:39 2021

@author: 44797
"""

class Solution():
    def __init__(self):
        self.res = None
        
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        n, self.res = len(coins), 2**31-1
        
        def dfs(point, remainder, count):
            if not remainder:
                self.res = min(self.res, count)
                
            
            for i in range(point, n):
                if coins[i] <= remainder < coins[i] * (self.res-count):
                    dfs(i, remainder-coins[i], count+1)
        
        
    
        for i in range(n):
            dfs(i, amount, 0)
        
        return self.res
        
print(Solution().coinChange([27,398,90,323,454,413,70,315],6131))