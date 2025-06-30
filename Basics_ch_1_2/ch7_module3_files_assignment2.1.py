# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:28:40 2024

@author: tchatty
"""

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
a = 0
number=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    colpos = line.find(':')


    number = float(line[colpos+1:])
    count = count + 1
    a = a + number


average = a / count
print ('average:',average)