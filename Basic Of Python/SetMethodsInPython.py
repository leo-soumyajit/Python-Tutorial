#Set Methods in Python Programming

#uninon() method
set1 = {1,2,3,4}
set2 = {1,11,12,13}
set3 = set1.union(set2)
print(set3)

#update()
set1 = {1,2,3,4}
set2 = {1,24,21,3}
print(set1,set2)
set1.update(set2) #add or update the values of set1 with set2
print(set1) #now set1 contains union value

#intersection and intersection_update()
s1 = {1,2,3,4,5}
s2 = {1,5,7,8}
print(s1.intersection(s2)) #gives the intersection value
print(s1,s2)
s1.intersection_update(s2) #update the intersection value to s1
print(s1) #now s1 contains only intersection value

#symmetric_difference and symmetric_difference_update()
sset1 = {1,2,3,4,10,12,35,70}
sset2 = {1,2,3,4,11,12,40,35}
print(sset1.symmetric_difference(sset2)) #print those values which is not present in the both sets
sset1.symmetric_difference_update(sset2) #now sset1 contains the symmetric values
print(sset1)

#difference()
cities1 = {"Kabul","Barcelona","Madrid","London"}
cities2 = {"Delhi","Mumbai","Dubai","Madrid","London"}
print(cities1.difference(cities2)) #prints the difference of the main set, main set means is mainset.difference(anyset)

#isdisjoint()
"""
      checks both sets are contains different elements,
      if they contain any same element then it returns false
"""
set10 = {1,2,3,4,5}
set11 = {10,11,12,13,13}
print(set10.isdisjoint(set11))

#issuperset() and issubset()
""" 
    issuperset():
    checks if all the items of a particular set 
    are present in the original set
    
    issubset():
    checks if all the items of a original set 
    are present in the particular set
"""
set12 = {1,2,3,4,5}
set13 = {1,2}
print(set12.issuperset(set13))
print(set13.issubset(set12))

#del keyword
fullSet = {"a","b","c","d"}
del fullSet #this keyword delete the entire set

#clear() method
fullSet = {"a","b","c","d"}
fullSet.clear() #clears entire sets value and gives us empty set
print(fullSet)




