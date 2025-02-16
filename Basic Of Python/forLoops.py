# name = input("Enter name : \n")
# for i in name:  ## for String
#     print(i,end=" ")
#
# list = ["kanu","sinu","nunu"]
# for i in list:  ## for List
#     print(i , end=" ")
#
# number1 = int(input("Enter number : "))
# for i in range(number1):  ## range() for number values
#     print(i) ## starts from 0-number-1
#     print(i+1) ## starts from 1-number
#
# number2 = int(input("Enter number : "))
# for i in range(1,number2): ## starts from 1 - number-1 , if number+1 then 1-number
#     print(i)
#
# number3 = int(input("Enter number : "))
# for i in range(1,number3,2): ## step is for omit some number if 2 means jump 2 for every iteration
#     print(i)


#for loop with Else in Python


for i in range(1,6):
    print(i)
else:
    print("No i")
"""
    after all the iteration is completed
    the else block will executed
"""
for i in range(7):
    print(i)
    if(i==4):
        break
else:
    print("No i") # it will not execute as the loop is broken not completed






