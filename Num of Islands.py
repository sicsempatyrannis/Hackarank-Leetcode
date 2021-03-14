# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:18:41 2021

@author: 44797
"""




def numIslands(grid):
    
    ans = 0
    R, C = len(grid), len(grid[0])
    
    def explore(r, c):
        grid[r][c] = "0"
        if r + 1 < R and grid[r + 1][c] == "1": explore(r+1, c)
        if r - 1 >= 0 and grid[r - 1][c] == "1": explore(r-1, c)
        if c + 1 < C and grid[r][c + 1] == "1": explore(r, c+1)
        if c - 1 >= 0 and grid[r][c - 1] == "1": explore(r, c-1)
        
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1":
                ans += 1
                explore(r, c)
                
    return ans

    

grid = [["1","0","1","1","0","1","1"]]

print(numIslands(grid))