# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:00:51 2021

@author: 44797
"""
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        
        

    def put(self, key: int, value: int) -> None:
        
            self.cache[key] = value
            self.cache.move_to_end(key)
                   
            if len(self.cache) > self.capacity:
                self.cache.popitem(last = False)