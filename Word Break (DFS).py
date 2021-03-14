# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:23:31 2021

@author: 44797
"""

#### Improve for memoization ####
# import copy
import time
import collections
from functools import lru_cache
class Solution:
    def __init__(self):
        self.output = []
        self.wordDict = None
        
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = collections.defaultdict(list)
        if not s:
            return [[]]
        
        @lru_cache
        def _wordBreak(s):
            if not s:
                return [[]]
            
            for end_index in range(1, len(s)+1):
                word = s[:end_index]
                if word in wordSet:
                    for sub in _wordBreak(s[end_index:]):
                        memo[s].append([word] + sub)
                        
            return memo[s]
        
        
        _wordBreak(s)
        
        return [' '.join(words) for words in memo[s]]
        # self.wordDict = wordDict
        
        # if not s:
        #     return []
        
        # add_spaces = set()
        
        
        # for i in range(len(s)):
        #     if s[:i] in self.wordDict or s[i:] in self.wordDict:
        #         add_spaces.add(i)
                
        # if len(set(s)) == 1 and s[0] in wordDict:
        #     add_spaces = [i for i in range(len(s))]
            
        # print(add_spaces)   
        # def dfs(string, poss_spaces):
        #     check = string.split(' ')
          
        #     if set(check).issubset(self.wordDict) and string not in self.output:
        #         self.output.append(string)
        #         return string
        
        #     elif poss_spaces:
        #         for j in poss_spaces:
        #             new_string = string[:j] + ' ' + string[j:]
        #             remaining_spaces = copy.deepcopy(poss_spaces)
        #             remaining_spaces.remove(j)
        #             remaining_spaces = [t+1 for t in remaining_spaces]
        #             dfs(new_string, remaining_spaces)
                    
            
                
        # dfs(s, add_spaces)
        
        # return self.output
        
        
sol = Solution()
s = "aaaaaaaa"
words = ["aaaa","aa","a"]
expected = ["a a a a a a a a","aa a a a a a a","a aa a a a a a","a a aa a a a a","aa aa a a a a","aaaa a a a a","a a a aa a a a","aa a aa a a a","a aa aa a a a","a aaaa a a a","a a a a aa a a","aa a a aa a a","a aa a aa a a","a a aa aa a a","aa aa aa a a","aaaa aa a a","a a aaaa a a","aa aaaa a a","a a a a a aa a","aa a a a aa a","a aa a a aa a","a a aa a aa a","aa aa a aa a","aaaa a aa a","a a a aa aa a","aa a aa aa a","a aa aa aa a","a aaaa aa a","a a a aaaa a","aa a aaaa a","a aa aaaa a","a a a a a a aa","aa a a a a aa","a aa a a a aa","a a aa a a aa","aa aa a a aa","aaaa a a aa","a a a aa a aa","aa a aa a aa","a aa aa a aa","a aaaa a aa","a a a a aa aa","aa a a aa aa","a aa a aa aa","a a aa aa aa","aa aa aa aa","aaaa aa aa","a a aaaa aa","aa aaaa aa","a a a a aaaa","aa a a aaaa","a aa a aaaa","a a aa aaaa","aa aa aaaa","aaaa aaaa"]
start = time.time()
my_sol = sol.wordBreak(s, words)
end = time.time()
print(end - start)
print(my_sol)
               