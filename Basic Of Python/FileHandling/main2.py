f = open('myFile.txt','r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)


f = open('newFile.txt','r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f = open('newFile.txt','w')
lines = ["This is 1st line \n","This is 2nd Line \n","This is 3rd line"]
f.writelines(lines)
f.close()