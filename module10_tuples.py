# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 17:08:04 2025

@author: tchatty
"""

#tuples are immutable
#sorted function works through a sequence and gives you a sorted list
# d = {'a':10, 'c':22, 'b':1}
# print(d.items())
# print(sorted(d.items()))
# for k,v in sorted(d.items()):
#     print(k,v)
# tmp = list()
# for k,v in d.items():
#     tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
# print(sorted([(v,k) for k,v in counts.items()], reverse=True))
lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val,key in lst[:10]:
    print(key,val)

    