# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:13:32 2025

@author: tchatty
"""

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count=0
words=[]
for line in fh:
    words = line.rstrip().split()
    if not len(words) < 2 and words[0] == 'From': #check for lines starting with 'From' and if the line is longer than 2 positions 
        print(words[1])
        count=count+1
    else:
        continue
print('There were', count, 'lines in the file with From as the first word')