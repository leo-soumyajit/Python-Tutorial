import os

#if new folder is not exists then
if not os.path.exists("new"):
    os.mkdir("new") #create "new" folder

#create 100 folder inside "/new"
for i in range(1,101):
    os.mkdir(f"new/Day{i}") #name is Day {i}
    # os.rmdir(f"new/Day{i}") #for delete os.rmdir()

