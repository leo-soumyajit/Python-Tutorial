#Exception Handling in Python
from xml.dom import InvalidCharacterErr

a = input("Enter number : ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except ValueError as e:
    print(e) #it prints invalid literal for int() with base 10: {Your Invalid Input}
except IndexError as e: #can add multiple except
    print(e)
print("codes.........")

#try except in func
def div(x,y):
    try:
        return x/y
    except Exception as ex: # handle exception here
        print(ex)

print(div(10,0))

#with raise keyword
def div(x,y):
    if y == 0:
        raise Exception("Cant divide by zero")
    return x / y
try:
    print(div(10, 0))
except Exception as e:
    print(e)

#Finally clause
"""
    finally is init after try and except block
    it executes every time whatever error is occurred in try except block or not
"""
def func():
    try:
        ls = [1,2,3,4]
        i = int(input("Enter index to print value : "))
        print(ls[i])
        return 1
    except ValueError:
        print("Some Value error occurred..")
        return 0
    except IndexError:
        print("Some Index error occurred..")
        return 0
    finally:
        print("No matter what im always executed")
        #this finally block will always execute whether func() returned or not

x = func()
print(x)

