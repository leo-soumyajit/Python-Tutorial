class Student:
    def __init__(self,n,r):
        print("This is a constructor")
        self.name = n
        self.roll = r
        Student.info(self) #call the method in the constructor

    def info(self):
        print(f"Name of student is : "
              f"{self.name}, Roll number is : {self.roll}")

obj1 = Student("SOUMYAJIT BANERJEE","23/IT/166")
# obj1.info()


class Department:
    def __init__(self,name): #constructor using param
        self.name=name
        print(name)

obj2 = Department("INFORMATION TECHNOLOGY")


