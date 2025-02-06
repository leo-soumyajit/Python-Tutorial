import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if(timestamp>="07:00:00" and timestamp<="11:59:00"):
    print("Good Morning sir")
elif(timestamp>="17:00:00" and timestamp<="20:59:00"):
    print("Good evening sir")
else:
    print("Good night sir")