# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:23:32 2025

@author: tchatty
"""

#ccc = dict()
#ccc['csev']=1
#ccc['cwen']=1
#print(ccc)
#ccc['cwen']=ccc['cwen']+1
#print(ccc)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

#using the get method
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)