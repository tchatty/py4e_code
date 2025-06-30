# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:54:08 2024

@author: tchatty
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum 
    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum

print('Maximum is', largest)
print('Minimum is', smallest)