x = 10
k=1

def myFunc():
    global x #to modify the global variable value
    x = 11
    y = 5
    print(y)
    print(k) #global variable can access everywhere

myFunc()
print(x)