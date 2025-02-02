# Explicit (Narrowing)
a = 10
b = "10"
string_number = int(b)
res = string_number+a
print(res)
c = "10"
d = "10"
result = (int(c)+int(d))
print(result)

"""
    Explicit typeCasting : 
    the typeCasting is done by Explicitly by developer 
    it converts large level data types to small level data types
"""


#Implicit typeCasting
x = 10 #int
y = 10.10 #float
print(type(x+y),x+y) #float
"""
    Implicit typeCasting : 
    python converts smaller range datatypes to 
    larger range data types automatically
"""
