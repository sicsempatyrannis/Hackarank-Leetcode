# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:16:39 2021

@author: 44797
"""

class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        room = 0
        available = 0
        s_ptr = e_ptr = 0
        while s_ptr != len(intervals):
            if starts[s_ptr] < ends[e_ptr]:
                if available == 0:
                    room += 1
                else:
                    available -= 1
                s_ptr += 1
            else:
                available += 1
                e_ptr += 1
        return room