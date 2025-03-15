class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    @property
    def name_getter(self):
        return self.name

    @name_getter.setter
    def name_setter(self,name):
        self.name = name

    @property
    def roll_getter(self):
        return self.roll

    @roll_getter.setter
    def roll_setter(self,roll):
        self.roll = roll


    def info(self):
        print(self.name_getter,self.roll_getter)



obj = student("Soumya","166")
obj.name_setter="Soumyajit"
obj.roll_setter ="166"
print(obj.name_getter)
obj.info()