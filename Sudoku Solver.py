# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 04:37:23 2020

@author: 44797
"""

def sudokuSolver(board):
    empty = emptySpaces(board)
    
    for i in empty:
        row = rowCheck(i, board)
        col = colCheck(i, board)
        box = squareCheck(i, board)
        
        
    pass

def rowCheck(position, board):
    nums = []
    for i in range(1, 10):
        if i not in board[position[0]]:
            nums.append(i)
            
    return nums

def squareCheck(position, board):
    nums = []
    box_x = position[1] // 3
    box_y = position[0] // 3

    present_nums = [board[i][j] for i in range(box_y*3, box_y*3 + 3) for j in range(box_x * 3, box_x*3 + 3)]
    for i in range(1, 10):
        if i not in present_nums:
            nums.append(i)
            
    return nums

def colCheck(position, board):
    nums = []
    present_nums = [board[i][position[1]] for i in range(9)]
    for i in range(1, 10):
        if i not in present_nums:
            nums.append(i)
            
    return nums
    
def emptySpaces(board):
    empty = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                empty.append((i,j))
            
    return empty

def finalCheck(colBased, rowBased, boxBased):
    poss_moves = []
    for i in range(1, 10):
        if i in colBased and i in rowBased and i in boxBased:
            poss_moves.append(i)
            
    return poss_moves
    