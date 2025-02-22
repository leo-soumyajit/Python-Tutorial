import os

#rename the directories source -> destination
for i in range(1,101):
   os.rename(f"new/Tutorial{i}",f"new/Tutorial {i}")