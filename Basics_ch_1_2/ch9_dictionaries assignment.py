# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 15:46:46 2025

@author: tchatty
"""

#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

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
    email = words[1]
    counts[email]=counts.get(email,0)+1
#print(counts)

max_email = None
max_count = None
for email,count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count
print(max_email,max_count)
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword,bigcount)