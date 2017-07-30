import glob
import os
import time

searchedfile = glob.glob("/home/iamkj03/*")
files = sorted( searchedfile, key = lambda file: os.path.getmtime(file))

for file in files:
 print("{} - {}".format(file, time.ctime(os.path.getmtime(file))) )
