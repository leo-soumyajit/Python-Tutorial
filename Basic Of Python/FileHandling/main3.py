f = open('demoFile.txt','r')
f.seek(9) #now it prints after 9 value
print(f.read(5)) #print 5 char after 9
print(f.tell()) #prints the current pos

f = open('demo2.txt','w')
f.write("Hello Bhai !")
f.truncate(7)

f = open('demo2.txt','r')
print(f.read())