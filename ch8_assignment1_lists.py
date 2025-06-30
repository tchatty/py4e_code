# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:13:48 2025

@author: tchatty
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.rstrip().split()
    for word in words:
        if word not in lst: 
            lst.append(word)
lst.sort()
print(lst)


