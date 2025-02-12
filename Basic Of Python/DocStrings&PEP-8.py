#Introduction to Docstring and PEP-8
#add docString above the function body

def square(n):
    '''
        :param n:Takes in a number n
        :return:square of number n
    '''
    return n**2
print(square(5))
print(square.__doc__)

#PEP - 8
"""
    <import this> in cmd 
    it shows a poem
    The Zen of Python by Tim Peters
"""

