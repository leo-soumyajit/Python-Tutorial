number = int(input("Enter number : "))
for i in range(100):
    if i == 0: continue #skip the iteration
    print(number, "X",i,"=",number*i)
    if i==10:
        break           #break the loop
print("Loop ke bahar ageyaa...")
