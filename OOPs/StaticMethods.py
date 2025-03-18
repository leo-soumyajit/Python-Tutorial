class Math:
    def __init__(self,num):
        self.num = num

    def addition(self,n):
        self.num = self.num+n
        pass

    @staticmethod
    def add(a,b):#don't need to use self keyword here
        return a+b

m = Math(10)
print(m.num)
m.addition(10)
print(m.num)
print(Math.add(10,0)) #can be accessed by using class name Directly

