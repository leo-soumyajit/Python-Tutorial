#comparison operators
#is -> checks memory location
#== -> checks content value

a = 4
b = 4
print(a is b) #true->location same as integers/strings/tuples are immutable
print(a==b) #true-> value same

c = [1,2,3]
d = [1,2,3]
print(c is d) #false->location change as list is mutable
print(c == d)#true-> content same

