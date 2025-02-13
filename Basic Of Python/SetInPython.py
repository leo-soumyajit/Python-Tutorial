#Introduction to Set in Python
#only contains unique elements

sets = {"kanu","titu","roy","kanu"}
sets.add("afgan")
sets.remove("roy")
print(set.__doc__)
newSet = sets.copy()
print(sets)
print(newSet)

"""
    emptySet = {}           is a type of dict 
    print(type(emptySet))   o/p : <class 'dict'>
    we can create empty set using set()
    s = set()
    print(type(s))          o/p : <class 'set'>
"""

#taking user input in set
sets = set(input("enter : ").split())
print(sets)
