# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:46:09 2022

@author: dell
"""

#ARRAYS
#easier for finding index

import array as arr

#creating array (O(1))
a = arr.array('i', [1,2,3])
print(a)
f = arr.array('d', [1.0, 2.0, 3.0])
print(f)

for i in range(3):
    print(a[i])
    print(f[i])


#inserting elements
a.insert(0,0)    #O(n)
print(a)
f.append(4.0)    #O(1)
print(f)


#accessing elements from array (O(1))
print(a[0])


#deleting elements from array (O(1) for removing last element, O(n) for removing other element)
print(a.pop(1))
a_ = arr.array('i', [1,2,3,4,5,6,4,3,1,2,4])
a_.remove(1)    #removes first occurrence
print(a_)


#searching in array (O(n))
print(a.index(2))