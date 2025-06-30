# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 17:37:19 2025

@author: tchatty
"""

name = input('Enter file:')
try:
    handle = open(name)
except:
    print('File cannot be opened:', name)
    quit()
    
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    hour = words[5].split(":")
    hour = hour[0:1]
    for count in hour:
        counts[count]=counts.get(count,0)+1
#print(counts)
lst = list()
for k,v in counts.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)
        
    #counts[email]=counts.get(email,0)+1