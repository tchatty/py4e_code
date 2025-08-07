#xml is an intermediate protocol to send data from one location to another across the web.
#Converting our internal structure into the interchange structure is called serialization
#It is de-serialized on the other end. xml has start & end tags, content, and attributes on the start tags.
#text nodes and attribute nodes are children of the parent nodes. There can be many attribute nodes.

import urllib.request
import xml.etree.ElementTree as ET
import ssl
#''' refers to a multi-lined string
def practice_1():
    data = '''<person>
        <name>Chuck</name>
        <phone type = "int">
            +1 732 303 4456
        </phone>
        <email hide = "yes"/>
        </person>'''

    tree = ET.fromstring(data) #takes the multi-lined string into a tree
    print('Name:', tree.find('name').text)#finds the information in tag 'name' and returns the text
    print('Attr:', tree.find('email').get('hide'))

def practice_2():
    input = '''<stuff>
        <users>
            <user x = "2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x = "7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''
    stuff = ET.fromstring(input)
    lst = stuff.findall('users/user')
    print('User Count:', len(lst))
    for item in lst:
        print('Name:', item.find('name').text)
        print('ID:', item.find('id').text)
        print('Attr:', item.get('x'))

def assignment_xml():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL:')
    if len(url)<1:
        url = 'http://py4e-data.dr-chuck.net/comments_42.xml' #default

    print('Retrieving',url)
    uh = urllib.request.urlopen(url) #read url into a handle
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data) #read xml data into a tree

    counts = tree.findall('.//count')#find all tags 'count'
    nums = list()
    for count in counts:
        print(count.text)
        nums.append(int(count.text))#add text in count tags as an integer to the nums list
    print('Count:', nums)
    print('Sum:', sum(nums))
assignment_xml()