def function(fx):
    def wrapper():
        print("Print before function call")
        fx()
        print("Print after function call")
    return wrapper

@function
def hello():
    print("Hello ji")

hello()
print() #for space
#another way without using @function
# function(hello)()

def greet(fx):
    def wrapper(*args , **kwagrs ):
        print("Good morning")
        fx(*args,**kwagrs)
        print("Thanks for using this function")
    return wrapper

@greet
def addition(a,b,c):
    print("Sum is : ",a+b+c)

addition(1,2,3)
print() #for space
