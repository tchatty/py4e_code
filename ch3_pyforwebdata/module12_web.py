#ASCII was the most popular encoding in the early days of the internet
#the ordinals of lower case letters were higher than upper case letters
#unicode has characters for all different languages
#UTF-8 is the recommended practice for encoding data to be exchanged between systems
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
def block_1():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #allows you to treat urls as files
    # for line in fhand:
    #     print(line.decode().strip())
    counts = dict()
    for line in fhand:
        words = line.decode().split()
        for word in words:
            counts [word]=counts.get(word, 0)+1
    print(counts)
#block_1()
#web scraping is a program / script that retrieves information. Beautiful soup deals with
def block_2():
    url = input('Enter URL:')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser') #parses the html into a tree

    tags = soup('a') #retrieve all the anchor tags in the document
    for tag in tags:
        print(tag.get('href',None))
#block_2()

def block_3():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = input('Enter URL:')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')#converts html page into an object
    tags = soup('a')
    for tag in tags:
        print(tag.get('href',None))
block_3()
