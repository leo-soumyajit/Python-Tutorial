i = 1           #initialization
while(i<=5):    #condition
    print(i)
    i+=1 # i = i+1 #increment/decrement otherwise loop never ends(infinite Loop)
print("Loop end here...")

#we can also use else block
count = 5
while(count>0):
    print(count)
    count-=1 #decrement
else:
    print("Loop end here...im in else block")



#accumulate do-while in Python (Py doesn't support do-while)
while True:
    i = int(input("Enter number : "))
    print(i)
    if i<=10:
        break
print("Loop done here...")














