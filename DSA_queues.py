# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 18:11:02 2022

@author: dell
"""

#QUEUES

#deque for faster append/pop (O(1))
from collections import deque

q = deque()


#adding elements
q.append('a')
q.append('b')
q.append('c')
print(q)

#removing elements
print(q.popleft())
print(q)


#other functions
from queue import Queue
q = Queue(maxsize = 3)
q.put('a')
q.put('b')
q.put('c')
#removes and returns element
print(q.get())
print(q.get())
print(q.get())
#boolean for if queue is empty/full
print("\nEmpty: ", q.empty())
print("Full: ", q.full())


#priority queue (O(logn))
from queue import PriorityQueue
q = PriorityQueue()

q.put(4)
q.put(2)
q.put(1)
q.put(3)
while not q.empty():
    next_item = q.get()
    print(next_item)
    
q.put((4, 'a'))
q.put((2, 'c'))
q.put((1, 'd'))
q.put((3, 'b'))
while not q.empty():
    next_item = q.get()
    print(next_item)