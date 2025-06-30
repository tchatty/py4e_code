# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:01:13 2024

@author: tchatty
"""
fhand = open('mbox.txt') #file handle is a sequence of lines that we can iterated through with a for loop. It is a connection to the file's data.
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

xfile = open('mbox-short.txt') #the .read method can read the whole file (including new lines) into a single string
inp = xfile.read()
print(len(inp))
print(inp[:20])

for fromline in xfile:
    fromline = fromline.rstrip() #deletes the extra white space between the results
    if line.startswith('From:'): #startswith is a method that enables searching for lines that start with a specific thing
        print(fromline)
    
#Another way to do the above is to skip lines that don't start with a specific thing

for fromline in xfile:
    fromline = fromline.rstrip()
    if not line.startswith('From:'):
        continue
    print(fromline)
    
# Can use in to find a line with a string within it

for inline in xfile:
    inline = inline.rstrip()
    if not '@uct.ac.za' in inline:
        continue
    print(inline)
    
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)