# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 14:03:51 2025

@author: tchatty
"""
#Making a list
# cards = list()
# cards.append(12)
# cards.append(3)
# cards.append(75)
# print (cards[1])

#Making a simple dictionary
# cabinet = dict()
# cabinet['summer']=12
# cabinet['fall']=3
# cabinet['spring']=75
# print(cabinet)
# print(cabinet['fall'])

#Creating counters 
# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)

#counting with if else
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name]=counts[name]+1
# print(counts)        

#counting with get
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     counts[name]=counts.get(name,0)+1
# print(counts)

#counting from a line of text
# counts = dict()
# print('Enter a line of text:')
# line = input('')

# words = line.split()
# print('Words:', words)

# for word in words:
#     counts[word] = counts.get(word,0)+1
# print('Counts', counts)

#dictionaries and files
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
        
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)

    