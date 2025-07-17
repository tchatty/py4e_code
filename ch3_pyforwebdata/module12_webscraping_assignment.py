import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
def assignment_1():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = input('Enter URL:')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')  # converts html page into an object
    tags = soup('span')
    s = list()
    for tag in tags:
        s.append(int(tag.string))
    print('Count:',len(s))
    print('Sum:',sum(s))

def assignment_2():
    #The program will use urllib to read the HTML from the data files below,
    # extract the href= values from the anchor tags,
    # scan for a tag that is in a particular position relative to the first name in the list,
    # follow that link and repeat the process a number of times and report the last name you find.
    #ignore SSL/TLS certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #input url, count, and position
    url = input('Enter URL:')
    count = int(input('Enter count:'))
    position = int(input('Enter position:')) - 1 #convert to 0-based index

    #Loop through the process
    for i in range(count+1):
        print('Retrieving:', url)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        #extract all anchor tags
        tags = soup('a')
        hrefs = [tag.get('href', None) for tag in tags]

        #update url to the one at the desired position
        if len(hrefs)> position:
            url = hrefs[position]
        else:
            print('Not enough links on this page')
            break
assignment_2()