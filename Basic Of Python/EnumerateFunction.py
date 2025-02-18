#Enumerate function

l = [71,18,48,50,78,90,96,87]
for i,val in enumerate(l):
    print(i,val)
    if i==6:
        print("Soumyajit, Awsm")
print()

#Change the start index
ls = [1,2,2,3,4,2,5,6,2,1,7]
for i,val in enumerate(ls,start=4):
    print(i,val)