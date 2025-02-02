#length function in Python
names = "Kanu,Soumyajit"
print("Length of",names,"is :",len(names))

#String Slicing
"""
    varname[first_idx : last_idx] 
    first_idx inclusive
    last_idx exclusive
"""
name = "Mango"
print(name[0:3])


#balnk index details
"""
    Python automatically adds 0 before and length(var) after 
    if we are not provide anything
    var[:] -> equivalent to var[0:length(var)]
"""
ex = "Fruit"
print(ex[:])


#Negetive Slicing
"""
    python adds string length automatically before -number sign
    len(var)-4 : len(var)-2
"""
a = "Harry"
print(a[-4:-2])



