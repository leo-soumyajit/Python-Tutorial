#reduce
from functools import reduce

l = [1,2,3,4,5]
print(l)
s = reduce(lambda x, y: x + y, l)
print(s)

