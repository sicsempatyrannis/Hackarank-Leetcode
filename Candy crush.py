# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:21:28 2021

@author: 44797
"""
import numpy as np
class Candy():
    def __init__(self):
        self.board = None

    def candyCrush(self, board):
        
        self.board = np.array(board)
        print(self.board.shape)
        def checkCol(col, start):
            u = d = start[0]
            
            while u > 0:
                if col[start[0]] == col[u-1]:
                    u -= 1
                    self.checkRow(self.board[u, :], [u, start[1]])
                elif col[start[0]] != col[u-1]:
                    break
                
            while d < len(col):
                if col[start[0]] == col[d+1]:
                    d += 1
                    self.checkRow(self.board[d, :], [d,start[1]])
                elif col[start[0]] != col[d+1]:
                    break
                
            if crushCol(u, d, start[1]):
                moveZeros()
            
        
        def checkRow(row, start):
            l = r = start[1]
            print(start)
            while l > 0:
                if row[start[1]] == row[l-1]:
                    l -= 1
                    checkCol(self.board[:, l], [start[0], l])
                elif row[start[0]] != row[l-1]:
                    break
                    
            while r < len(row):
                if row[start[1]] == row[r+1]:
                    r += 1
                    checkCol(self.board[:, r], [start[0], r])
                elif row[start[0]] != row[r+1]:
                    break
               
            if crushRow(l, r, start[0]):
                moveZeros()
    
        def crushCol(u, d, col):
            if abs(u - d) >= 3:
                self.board[u:d, col] = 0
                print('crushed at ', self.board[u:d, col])
            
            else:
                return False
            
        def crushRow(l, r, row):
            if abs(l-r) >= 3:
                self.board[row, l:r] = 0
                print('crushed at ', self.board[row, l:r])
                return True
            
            else:
                return False
            
        def moveZeros():
            for i in len(self.board[0]):
                col = self.board[:, i][::-1]
                zero_count = 0
                i = 0
                while i < len(col):
                    if i == 0:
                        zero_count += 1
                        del col[i]
                    else:
                        i += 1
                  
                if zero_count > 0:
                    for _ in range(zero_count):
                        col.append(0)
                        
                self.board[:, i] = col[::-1]
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 0:
                    checkRow(self.board[i], [i,j])
                    checkCol(self.board[:, j], [i,j])


board = [[110,5,112,113,114],
         [210,211,5,213,214],
         [310,311,3,313,314],
         [410,411,412,5,414],
         [5,1,512,3,3],
         [610,4,1,613,614],
         [710,1,2,713,714],
         [810,1,2,1,1],
         [1,1,2,2,2],
         [4,1,4,4,1014]]

sol = Candy()
sol.candyCrush(board)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        