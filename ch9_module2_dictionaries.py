# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:28:57 2025

@author: tchatty
"""

counts = dict()
print('Enter a line of text')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts', counts)
#print(list(counts.values()))#using the values method
#print(list(counts.keys()))#using the keys method
print(list(counts.items()))

for aaa,bbb in counts.items():
    print(aaa,bbb)
    