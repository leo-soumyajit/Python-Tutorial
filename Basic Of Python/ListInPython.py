# #Introduction to List in Python
#
# list1 = [1,2,3,4,5,6,"Dhoni"]
# print(list1)
# print(list1[0]) #positive indexing starts from 0
#
# """
#     Negative indexing length of list -that given number
#     ex:
#         var[-3] == var[len(var)-3]
# """
# print(list1[-3])
#
# # check whether an item present in the list or not
# marks = [1,2,3,4,5]
# if int(input("Enter number")) in marks: #can use if-else like this way
#     print("Yes")
# else:
#     print("No")
#
# #jump index
# """
#     syntax = var[st : end : jumpIndex]
#     jumpIndex = jump over the index with the number give
# """
# # index   0        1       2        3        4
# name = ["Dhoni","Raina","Jadeja","Ashwin","Bravo"]
# print(name[0:len(name):3])

#List Comprehension
list = [item for item in range(4)]
print(list)

list = [item for item in range(10) if item%2==0]
print(list)

listName = ["India","China","USA","England","Russia"]
newList = [item for item in listName if "a" in item]
print(newList)

city = ["Kolkata","Noida","Pune","Bengaluru","Mumbai"]
newCity = [item for item in city if "o" in item]
print(newCity)













