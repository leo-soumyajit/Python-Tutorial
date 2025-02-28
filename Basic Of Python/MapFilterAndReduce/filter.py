#filter
#predicate means returns a boolean value
def predicate(a):
    return a%2==0 #like here it returns boolean value

l = [1,2,3,4,5,6,7,8]
print(l)
l = list(filter(predicate,l))
print(l)

#Using lambda
l = list(filter(lambda x:x%2==0,l))
print(l)