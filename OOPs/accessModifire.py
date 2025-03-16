


class Student:
    def __init__(self,name,roll):
        self.__name = name # add a indecator __variable means its private cant be accessed directly
        self._roll = roll # this is now protected var
        Student.__showDetails(self)
    def __showDetails(self): #this is private method
        print(f"Name is {self.__name} roll is {self._roll}")

class X(Student):
    pass

std1 = Student("Soumyajit",166)
# print(std1.__name)# private so cant be accessed directly
print(std1._Student__name) #can access private var like this object._ClassName__variable
print(std1._roll)
x = X("Kanu",123)
print(x._roll)#protected can used in his subclasses and his own class

