import os 
from os import path
import shutil
from zipfile import ZipFile

if path.exists("newfile.txt"):
     src = path.realpath("newfile.txt")
     dst = src + ".bak"
#shutil.copy(src, dst)
#rename the org file
# os.rename("textfile.txt", "newfile.txt")
# now put things into a ZIP archive
# root_dir, tail= path.split(src)
# shutil.make_archive("archive", "zip",root_dir)
with ZipFile("testzip.zip","w") as newzip:
    newzip.write("newfile.txt")
    newzip.write("textfile.txt.bak")