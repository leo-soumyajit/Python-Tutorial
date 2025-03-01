#classes is a blueprint/template from where objects are created

class Person:
    name = "Kanu"
    age = 20
    def info(self):
        print(f"{self.name}'s age is : {self.age}")

obj = Person()
print("Name is : ",obj.name)
print("Age is : ",obj.age)
#call the function
obj.info()
#change the value of attributes ;
obj.name="Soumyajit"
obj.age=21
print("Name is : ",obj.name)
print("Age is : ",obj.age)

