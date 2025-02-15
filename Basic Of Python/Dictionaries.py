#Introduction to Dictionaries in Python
#Combination of Key value pair
dic = {
    "Kanu":"A human Being",
    "Computer":"Electronic Devices",
    "Python":"Snake , Programming Language"
}
print(dic)

#can access the Value using key
print(dic["Python"]) #if key is not present then throws error
print(dic.get("Python")) #if key is not present then give None


#print all the key using for loop with in keyword
for i in dic.keys():
    print(i)

print(dic.keys()) #it also gives keys,
# like this(dict_keys(['Kanu', 'Computer', 'Python']))


#print all the values using for loop with in keyword
for val in dic:
    print(dic[val])

print(dic.values())#it also gives values,
# like this(dict_values(['A human Being', 'Electronic Devices', 'Snake , Programming Language']))

#print all key-value pairs
print(dic.items())

for key , value in dic.items():
    print(key,":",value) #gives key:value in log
