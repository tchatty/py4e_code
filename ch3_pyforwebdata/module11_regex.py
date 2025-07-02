#using regular expressions
#Cheat Sheet:
#Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

import re
def block_one():
    hand = open('mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('^From:', line):
            print(line)

#without using regular expressions
def block_2():
    hand = open('mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if line.find('From:') >= 0:
            print(line)

#matching and extracting data using regex
def block_3():

    x = 'My 2 favorite numbers are 19 and 42'
    a = 'From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008'
    y = re.findall('[0-9]+',x)
    z = re.findall('a+?',x)
    b = re.findall('^From (\S+@\S+)',a)
    c = re.findall('^From .*@([^ ]*)', a)
    print(y)
    print(c)
    print(b)
    print(z)
#be careful of greedy matching. Extracting a string using findall when you use * or + it will pull the largest string possible.
#The ? character ensures that it is not greedy. '[aeiou]+?'

def block_4():
    hand = open('mbox-short.txt')
    numlist = list()
    for line in hand:
        line = line.rstrip()
        stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #check for lines that start with the phrase, space, one or more floating point number
        if len(stuff) !=1: continue #skip the line if there is more than one floating point numbers
        num = float(stuff[0])
        numlist.append(num)
    print('Maximum:', max(numlist))

#block_3()