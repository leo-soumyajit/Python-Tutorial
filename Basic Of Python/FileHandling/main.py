#Introduction to File IO in Python

#r -> read
f = open('myFile.txt','r')
print(f.read())#to read file
f.close()

#write
f = open('myFile.txt','w')
f.write("This is modified file\n")
f.close()
#write this text but previous text is replaced

#append
f = open('myFile.txt','a')
f.write("Hei this is a new line") ##append this text
f.close()

#create new file
# fileNew = open('newFile.txt','x')

#with keyword
with open('newFile.txt','a') as newfile:
    newfile.write("Just Added this line")
with open('newFile.txt','r') as newfile:
    print(newfile.read())