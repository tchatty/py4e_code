# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:11:19 2025

@author: tchatty
"""

total = 0
count = 0
while True:
    inp = input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('The average is:', average)

numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print('The average is', average)
    
    