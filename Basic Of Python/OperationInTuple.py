#Operations in Tuple

""""
    since Tuples are immutable so we cant directly manipulate 
    we have to convert a Tuple into a list by list() method 
    then we can do operations.
    after operations are done we can convert list -> tuple
    by using tuple() method
"""""

country = ("India","Germany","Russia","England")
print(country)
listCountry = list(country) #convert into List
listCountry.append("USA") #then can manipulate
print(listCountry)
listCountry.pop(2) #used to delete via index
print(listCountry)
listCountry.remove("England") #used to delete via value
print(listCountry)
country = tuple(listCountry) #convert tuple back
print(country)

#count method
numbers = (1,2,2,1,3,5,1,2,3,5,10,3,5,7,8,10)
print(numbers.count(1)) #count the number value
#index()
print(numbers.index(3)) #return the first(index) occurrence of the given number
print(numbers.index(3,5,10)) #can pass the element and also st indx or end indx for range
#len() for length of tuple
print(len(numbers))


