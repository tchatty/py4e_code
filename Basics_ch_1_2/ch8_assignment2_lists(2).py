# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:15:14 2025

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
    line = line.rstrip()
    if line.startswith('From:'): 
        count = count + 1
        words = line.split()
        for x in words:
            email = words[1]
            print(email)
print('There were', count, 'lines in the file with From as the first word')
  