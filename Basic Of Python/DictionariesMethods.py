#Dictionary methods
#update() to update Dict
employee = {
    '101':"Soumyajit",
    '102':"Arjun",
    '103':"Ram",
    '104':"Zakir",
    '105':"Tritiya",
}
print(employee)
employee.update({'106':"Shyam"})
print(employee)
#we can update with 2 dict
employee2 = {
    "10010":"Raja"
}
employee.update(employee2) #now employee contains employee2 also
print(employee)
print(employee2)

#clear() for clear the entire Dict
dic = {
    "Bengal":"Kolkata",
    "Bihar":"Patna",
    "Maharashtra":"Mumbai,Pune,Nagpur",
}
dic.clear() #clears entire Dict value and gives us empty Dict
print(dic) #empty dict

#pop() remove the key:value pair whose key value is passed as param
dic = {
    '1':"Kanu",
    "2":"Tittu"
}
print(dic)
dic.pop("2") #removes the given key
print(dic)

#popitem() : remove the last item in the dict
emp = {
    '101':"Soumyajit",
    '102':"Arjun",
    '103':"Ram",
    '104':"Tritiya",
    '105':"Zakir",
}
emp.popitem()
print(emp) #removes the last key:val pair of the dict

#del keyword
"""
    del keyword is used to delete dict or any key:val of dict
    del dict["key"] removes only key:val
    del dict removes the entire dict
"""
admin = {
    "10010":"Raja",
    "182882":"Koushik",
    "72717":"RamuBhai"
}
del admin["72717"] #now 72717:RamuBhai no longer exists
print(admin)
del admin #now admin dict is no longer exists
