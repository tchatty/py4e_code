# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:39:02 2024

@author: tchatty
"""

score = input("Enter Score: ")
s = float(score)
if s > 1 or s <0:
    print ("value is out of range")
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
else:
    print("F")
    
    