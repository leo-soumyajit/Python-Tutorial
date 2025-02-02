#double quotes
from codecs import namereplace_errors

name = "Soumyajit"
print("Name is :",name)

#single quotes
print('Kanu is hehehe \"hi bro\"')

## using triple double quotes(Multiline String)

#accessing the Character in a String
name = "Soumyajit"
print(name[0]) #indexing starts from 0 -> S here

dog = """
    Dog is a pet animal. 
    It is the oldest friend of human beings. 
    It watches our house. 
    It is very faithful animal and never left his master. 
    It is used by police to fight crime. 
    Sheep- rearers also use them. 
    Thus it is useful for us in many ways
"""
print(dog)

#Itreate through a loop
for character in dog: ## prints all the character in that String
    print(character)