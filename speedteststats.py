#!/usr/bin/python
### speedtest analyst
### by memecian
###

import re
import os
from datetime import datetime

temp = datetime.now()
rightNow = temp.strftime("%H:%M %d-%m-%Y")
month = temp.strftime("%m-%Y")

# run speedtest
print(f"running speedtest ({rightNow})")
os.system("speedtest" + "> out.txt")
# open speedtest results
inFile = open("out.txt", "r")

# regex identifying whitespace preceding two numbers separated by a dot
# e.g.: [TAB]922.55 
RegPattern = re.compile("\s*(\d+\.\d+)")

# check if a directory already exists for this month or not, create a new one 
# if necessary.
# 
workingDir = os.getcwd()

if os.listdir(workingDir).__contains__(month) == False:
    print(f"Directory for {month} does not exist, creating.")
    try: 
        os.mkdir(month)
    except FileExistsError:
        print("actually, it does. Skipping..")

# else assume the directory exists and open the file.
outFile = open(f"./{month}/results.txt", "a")

# add boilerplate if file is new
if os.path.getsize(f"./{month}/results.txt") == 0:
    outFile.write("LATENCY\tDOWNLOAD\tUPLOAD\tTIME\n")

# iterate through results, grab the first 3 matches and leave
i = 0
results = []
for x in inFile:
#    print(x)
    if i != 3:
        tempMatch = re.search(RegPattern, x)
        if tempMatch != None:
            results.append(tempMatch.group())
            i += 1

# print results to table
for x in range(3):
    outFile.write(f"{results[x].lstrip()}\t")
outFile.write(f"{rightNow}\n")
outFile.close()
inFile.close()
os.remove("out.txt")
