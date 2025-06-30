# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:54:37 2024

@author: tchatty
"""
fname = input('Enter a file name:')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
for line in fh:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
        
