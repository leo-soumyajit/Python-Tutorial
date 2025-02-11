#Introduction to Tuples in Python Programming
#same as List but once we create a tuple we cant change the value of tuple
tup = (1,2,3)
print(tup)
print(type(tup))
#can access the index via list style [indexNumber]
print(tup[0])
"""
    we cant reassign the value of an index
    like 
        var[0] = anyNumber      this gives us exception
"""

#using if cond like List
tupl = (1,2,3,5,6,10)
if int(input("Enter number ")) in tupl:
    print("Yes")
else:
    print("No")

# t=("Kolkata","Gurgaon","Pune","Bengaluru")
# newT = [item for item in t if "o" in item]
# print(type(newT),newT)