import os

#print the list of folder that contains the directory
folders = os.listdir("new")

for i,val in enumerate(folders):
    print(i,val)