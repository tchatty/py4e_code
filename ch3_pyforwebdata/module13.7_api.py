import urllib.request, urllib.parse
import http
import json
import ssl

def api_practice1():
    serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input ('Enter location: ') #ask for a location
        if len(address) < 1: break

        address = address.strip() #cleans up the data
        parms = dict()
        parms['q'] = address #q parameter where q = address

        url = serviceurl + urllib.parse.urlencode(parms) #urlencoding takes place

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters', data[:20].replace('\n', '')) #prints the first 20 characters of the data

        try:
            js = json.loads(data) #json parse
        except:
            js = None

        lat = js['features'][0]['properties']['lat']
        lon = js['features'][0]['properties']['lon']
        print('lat', lat, 'lon', lon)
        location = js['features'][0]['properties']['formatted']
        print('Location:', location)

#api_practice1()

def api_practice2():
    serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')  # ask for a location
        if len(address) < 1: break

        address = address.strip()  # cleans up the data
        parms = dict()
        parms['q'] = address  # q parameter where q = address

        url = serviceurl + urllib.parse.urlencode(parms)  # urlencoding takes place

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters',
              data[:20].replace('\n', ''))  # prints the first 20 characters of the data

        try:
            js = json.loads(data)  # json parse
        except:
            js = None

        if not js or 'features' not in js:
            print('Download Error')
            print(data)
            break

        if len(js['features']) == 0:
            print('Object Not Found')
            print(data)
            break

    #print(json.dumps(js, indent=4))

        lat = js['features'][0]['properties']['lat']
        lon = js['features'][0]['properties']['lon']
        print('Latitude:', lat, 'Longitude:', lon)
        location = js['features'][0]['properties']['formatted']
        print('Location:', location)

#api_practice2()

def api_assignment():
    serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')  # ask for a location
        if len(address) < 1: break

        address = address.strip()  # cleans up the data
        parms = dict()
        parms['q'] = address  # q parameter where q = address

        url = serviceurl + urllib.parse.urlencode(parms)  # urlencoding takes place

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')  # prints the first 20 characters of the data

        try:
            js = json.loads(data)  # json parse
        except:
            js = None

        print(json.dumps(js["features"][0]["properties"]["plus_code"], indent=4))

api_assignment()