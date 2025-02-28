#map(func , iterable)

def cube(x):
    return x*x*x

l = [1,2,3,4,5,6]
print(l)
l = list(map(cube,l))
print(l)