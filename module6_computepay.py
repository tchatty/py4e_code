# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:38:36 2024

@author: tchatty
"""

def computepay(h, r):
    if h<=40:
        pay = h*r
    elif h>40:
        pay = (h-40)*r*1.5 + 40*r
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print("Pay", p)