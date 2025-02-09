"""
    :default argument
"""
def default(fName , mName, lName="Dhuni"):  #we can pass default values
    print("Hello",fName,mName,lName)
default("Mahendra","Singh","Dhoni") ##we can override the default value


"""
    :keyword argument 
"""
def keyword(a,b):
    print("Sum is",a+b)
keyword(b=10,a=11) # doesn't matter the ordering by using key, and we have to pass both key

"""
    :required argument 
"""

def Required(a,b):
    return a*b
print("Multiplication is",Required(10,10))  # we must pass the value of argument

def Sum(*number): # *number is stores in tuple
    sum = 0
    for i in number:
        sum += i
    print(sum)
Sum(1,2,3,4,5,6,7,8,9,10) # and here we pass the tuple value


def nameAsDict(**name): ## ** for dictionary
    print("Hello",name["fName"],name["mName"],name["lName"])

nameAsDict(fName="Laal",mName="singh",lName="chadda") # pass key value pair