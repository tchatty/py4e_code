# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:21:28 2024

@author: tchatty
"""

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
total = 0
number = []
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #converting string to float
    count = count+1
    f = float(line[21:])
    #adding all the float values to a list
    number.append(f)
    total =0
    #adding all the list items
    for f in number:
        total=total+f
avg = total/count
print("Average spam confidence:",avg)

