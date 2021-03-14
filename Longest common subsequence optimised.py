# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:33:45 2021

@author: 44797
"""
# def dfs(node, graph, vis, n):
    
#     vis[node] = True
    
#     for i in range(n):
#         if not vis[node]:
#             dfs(i, graph, vis, n)
        
#         if graph[node][i] == 1:
#             count += graph[node][i]
#             graph = graph[node+1:, i+1:]
#             break
        
#     return count

import numpy as np

def commonChild(s1, s2):
    dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    
    
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
            else:
                dp[i][j] = dp[i-1][j] if dp[i-1][j] > dp[i][j-1] else dp[i][j-1]
            
    return dp[len(s1)][len(s2)]
                
            
                
          
    
n = len('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS')
print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))

# test = 'SHINCHAN'

# for i, j in enumerate(test):
#     if j == 'C':
#         new = test[:i] + test[i+1:]
        
#         print(new)
#         break