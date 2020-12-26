# Simple auto move and rename screenshots using command line
# Julian Syaputra I

import os
import time
import shutil

init_path = "" # initial path, insert ur own screenshot path lol. format : C:/path/to/screenshot/folder
folder = input("Input the name of the destination folder: ") # folder name of the destination
dest = os.path.join(init_path, folder) # path to the destination folder

# Checks whether the folder exist
if not os.path.isdir(dest):
    print("Folder not found. Creating new one...")
    # Creates the folder
    os.makedirs(dest)
else:
    print("Folder already exist. New files will be moved to the existing folder...")

name = input("Input the name of the files: ") # name of each new files
print(f"New screenshots will be renamed to " + name + "x" + " with x equals to the file number")

count = 1
before = os.listdir(init_path)
while True:
    time.sleep(5)
    after = os.listdir(init_path)
    if len(after) != len(before):
        newfiles = [f for f in after if not f in before]
        for file in newfiles:
            file_name = name + str(count) + ".png" # Assuming the screenshot format is .png
            init_file_path = os.path.join(init_path, file) # location of the new file
            file_dest = os.path.join(dest, file_name) # destination of the new file
            shutil.move(init_file_path, file_dest)
            print(f"New file detected, renaming {file} to {file_name}")
            print("New file moved")
            print()
            count += 1
        before = after