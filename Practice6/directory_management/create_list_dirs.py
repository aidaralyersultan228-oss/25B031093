#1 Create nested directories
#2 List files and folders
#3 Find files by extension
import os
os.makedirs("ata-ana/bala/nemere")

files = os.listdir("directory_management")

for i in files:
    if i.endswith(".py"):
        print(i)

