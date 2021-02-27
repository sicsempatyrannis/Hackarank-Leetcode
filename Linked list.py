# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:38:58 2021

@author: 44797
"""
class Node():
    def __init__(self, data):
        self.node = data
        self.next = None
        
class linkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        
    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            
        else:
            end_node = self.traverse()
            end_node.next = Node(data)
        self.length += 1
        
    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node.next
        
        return prev_node
        
    def remove(self, data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.node == data:
            self.head = self.head.next
            self.length -= 1
            return True
            
        else:
            curr_node = self.head
            
            while curr_node.next != None:
                if curr_node.next.node == data:
                    next_node = curr_node.next
                    curr_node.next = next_node.next
                    self.length -= 1
                    return True
                
                curr_node = curr_node.next
        
        return False
    
    def visualise_llist(self):
        ret = []
        
        if self.head is None:
            raise Exception("List is empty")
        
        curr_node = self.head
        while curr_node is not None:
            ret.append(curr_node.node)
            curr_node = curr_node.next
        print(ret)
        
        
    def list_length(self):
        return self.length
        
        
        
llist = linkedList()
llist.prepend(3)
llist.prepend(2)
llist.add(5)
llist.prepend(9)
llist.remove(9)
llist.visualise_llist()

# print(llist.list_length())
        
        