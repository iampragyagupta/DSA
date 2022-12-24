# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 19:55:45 2022

@author: dell
"""

#{SETS}
#unordered collection of datatypes(mutable, no duplicates, multiple datatypes)
#SEARCHING OPTIMIZED

#creating a set
#blank set
set1 = set()
print(set1)

#curly braces
set2 = {1,2,3,4,2}
print(set2)

#from string
set3 = set("hiiamPragya")
print(set3)

#from list
set4 = set(["hi", "i", "am", "Pragya"])
print(set4)



#testing set properties
set_ = set([1,2,3,4,5,4,3,2,1,3,6,7])
print(set_)

set_1 = set([1,2,"hello", 4,5 ,"world"])
print(set_1)



#adding elements (O(1))
#single element
set_.add(8)
print(set_)
set_.add((9,10))
print(set_)

#multielemnt
set_.update([8,10, 11, 12])
print(set_)



#searching for element (O(1))
for i in set_1:
    print(i)
    
print("hi" in set3)



#removing elements (O(1))
set_.remove(7)
print(set_)

set_.discard(2)
print(set_)

set_.clear()
print(set_)


#other functions
print(set1.union(set2))
print(set2.issubset(set_1))
print(set_1.issuperset(set2))


#frozenset== imutable
set__ = frozenset(["hi", "i", "am", "Pragya"])
print(set__)