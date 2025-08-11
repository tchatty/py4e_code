#JSON is native to JavaScript.
import urllib.request, urllib.parse
import http
import json
import ssl
def practice_1():
    data = '''{
        "name": "Chuck",
        "phone": {
            "type": "intl",
            "number": "+1 732 647 6443"
        },
        "email": {
            "hide": "yes"
        }
    }'''

    info = json.loads(data)
    print('Name:', info['name'])
    print('Hide:', info['email']['hide'])

def practice_2():
    input = '''[
        {"id": "001",
        "x": "2",
        "name": "Chuck"
        },
        { "id": "002",
        "x": "7",
        "name": "Chuck"
        }
    ]'''
    info = json.loads(input)
    print('User count:', len(info))
    for item in info:
        print('Name:', item['name'])
        print('ID:', item['id'])
        print('Attribute:', item['x'])
#practice_2()

def json_assignment():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL:')
    if len(url) < 1:
        url = 'http://py4e-data.dr-chuck.net/comments_42.json'  # default

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)  # read url into a handle
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    #print(json.dumps(js, indent=4))
    nums = list()
    for item in js['comments']:
        nums.append(int(item['count']))
    print ('Number:', len(nums))
    print('Sum:', sum(nums))
json_assignment()
