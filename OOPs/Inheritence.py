class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"Name of the employee is {self.name} and "
              f"id is {self.id}")

class Programmer(Employee):

    def __init__(self, name, id,address):
        super().__init__(name, id)
        self.address = address

    def showLanguage(self):
        print("Default Language is Python and Java")


e = Employee("Kanu",12)
e.showDetails()
p = Programmer("Soumyajit",1,"Kolaghat")
print(p.address)
p.showDetails()
p.showLanguage()