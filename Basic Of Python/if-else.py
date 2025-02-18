#conditional statement
#ex 1
age = int(input("Enter your age : "))
if(age>=80):
    print("U should not drive")
elif(age>=18):
    print("u can drive")
else:
    print("u can drive")

#ex 2
num = int(input("Enter your number"))
if(num>0):
    print("This is a Positive Number")
elif(num==0):
    print("This is zero")
else:
    print("This is a Negative Number")

#ex 3 (nested if)
num = int(input("Enter your number"))
if(num>0):
    if(num<=10):
        print("Number is bw 1-10")
    elif(num>10 and num<=20):
        print("Number is bw 11-20")
    else:
        print("Number greater than 20")
elif(num==0):
    print("Number is zero")
else:
    print("number is negative")

#Short Hand if-else
a = 100
b = 1001
print(a) if a>b else print("=")if a==b else print(b)
print("A") if a>b else print("No B")

c = 9 if a>b else 0
print(c)










