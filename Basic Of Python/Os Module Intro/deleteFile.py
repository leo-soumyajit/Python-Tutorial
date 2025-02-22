import os

#if a file exits then delete
if os.path.exists("demoFile"):
    os.remove("demoFile")