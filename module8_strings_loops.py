# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:07:29 2024

@author: tchatty
"""

fruit = 'banana'
index = 0
for letter in fruit:
    print(index,letter)
    index = index + 1
    
index = 0
while index<len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index+1
    
s = 'Monty Python'
print(s[0:5])

if 'nana' in fruit:
    print("Yes!")

greet = 'Hello Bob'
zap = greet.lower() #.lower is a method in the object str
print(zap)
print(greet)
print(type(greet))
#print(dir(greet)) show me all the methods in the object str
pos = greet.find('na')
print(pos)
nstr = greet.replace('Bob', 'Jane')
print(nstr)

data = 'From teja.chatty@icloud.com Wed Aug 14'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

text = "X-DSPAM-Confidence:    0.8475"
stpos = text.find('0')
print(stpos)
endpos = text.find('5')
print(endpos)
extr = text[23:29]
print(float(extr))
