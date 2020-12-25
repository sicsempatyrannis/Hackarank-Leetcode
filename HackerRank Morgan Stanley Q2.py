# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:13:37 2020

@author: 44797
"""
import numpy as np
def dfs(node, graph, dp, vis, n, save_, price):
    vis[node] = True
    dp[node] = graph[node][node]
    
    for i in range(n):
        if not vis[node]:
            save_ -= price[i]
            dfs(i, graph, dp, vis, n, save_, price)
        
        if save_ > price[i] and node != i:
            dp[node] = int(max(dp[node], graph[node][node] + graph[i][i]))
        
    return dp

def selectStock(saving, currentValue, futureValue):
    n = len(currentValue) 
    
    mem = np.zeros(shape=(n,n))
    
    for i, j in enumerate(currentValue):
        mem[i][i] = futureValue[i] -currentValue[i]
        
    num = n
    track = [0] * n
    
    for i in range(n):
        bank = saving
        bank -= currentValue[i]
        dp = [0] * n
        vis = [False] * n
        print(dfs(i, mem, dp, vis, num, bank, currentValue))
        track[i] = dfs(i, mem, dp, vis, num, bank, currentValue)
   
    ret = 0
    
    for i in track:
        if max(i) > ret:
           ret =  max(i)
            
    return ret
            
print(selectStock(250, [175,133,109,210,97], [200,125,128,228,133]))
            
    
   

    
    
    