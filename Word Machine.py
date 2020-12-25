# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:34:20 2020

@author: 44797
"""
def push(arr, num):
    arr.append(num)
    return arr

def pop(arr):
    arr.pop(-1)
    return arr

def dup(arr):
    num = arr[-1]
    arr.append(num)
    return arr

def add(arr):
    num = sum(arr[-2:])
    arr.pop(-1)
    arr.pop(-1)
    arr.append(num)
    return arr

def subtract(arr):
    num = arr[-1] - arr[-2]
    arr.pop(-1)
    arr.pop(-1)
    arr.append(num)
    return arr

def wordMachine(string):
    ret = []
    string_list = string.split()
    
    
    for i in string_list:
        
        if i == "POP":
            if len(ret) > 0:
                ret = pop(ret)
            else:
                return -1
                
        elif i == "DUP":
            if len(ret) > 0:
                ret = dup(ret)
            else:
                return -1
            
        elif i == "+":
            if len(ret) > 1:
                ret = add(ret)
            else:
                return -1
            
        elif i == "-":
            if len(ret) > 1:
                ret = subtract(ret)
            else:
                return -1
            
        else:
            ret = push(ret, int(i))
            
            
    return ret[-1]
            
            
   
print(wordMachine("4 5 6 - 7 +"))           





