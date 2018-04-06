#!/usr/bin/python

import os

for dirpath, dirnames, filenames in os.walk("/home/student/Part3/"):
    print("Files in %s are:" % dirpath)
    for file in filenames:
        print("\t" + file)
    print("Directories in %s are:" % dirpath)
    for dir in dirnames:
        print("\t" + dir)
        
