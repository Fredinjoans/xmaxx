import os
from os import path
import time 
from datetime import datetime
print("item exists:", path.exists("textfile.txt"))
print("item is a file: ", path.isfile("textfile.txt"))
print("item is a directory: ", path.isdir("textfile.txt"))
#work with file paths
print("item's path: ", path.realpath("textfile.txt") )
print("item's  path and name: ", path.split(path.realpath("textfile.txt")))
#get the modification time

t =time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

#calculate how long ago
td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(f"it has been {td} since the file was modified ")
print(f"Or, {td.total_seconds()} seconds")