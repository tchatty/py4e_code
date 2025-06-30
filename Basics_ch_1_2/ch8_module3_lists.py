# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:54:05 2025

@author: tchatty
"""

fhand=open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):continue
    w = line.split()
    email = w[1]
    pieces = email.split('@')
    print(pieces[1])