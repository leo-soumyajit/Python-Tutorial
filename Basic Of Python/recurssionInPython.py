#Introduction to Recursion

def factorial(n):
    '''
    factorial function using recursion
    :param n: takes n as input
    :return: factorial of that number
    '''
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n - 1)  #formula

"""
    factorial(5) dry run --->
    5*factorial(4)
    5*4*factorial(3)
    5*4*3*factorial(2)
    5*4*3*2*factorial(1) now base case hits 1 return 1
    5*4*3*2*1 = 120 res
"""
n = int(input("Enter value : "))
print(factorial(n))
print(factorial.__doc__)

#fibonacci series
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2) #formula

n = int(input("Enter number value : "))
summ=0
for i in range(n):
    summ += fib(i)
    print(fib(i))
print("The sum of fibonacci series upto",n,"is :",summ)

