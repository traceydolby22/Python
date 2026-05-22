
import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    print(json.dumps(js, indent=4))
    #print(json.dumps(js['features'][0]['properties'], indent=4))
    
    getting_plus_code = js['features'][0]['properties']['plus_code']
    print(getting_plus_code)
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)

#import urllib.request, urllib.parse, json, http, ssl

#from flask import ctx

#serviceurl = "https://py4e-data.dr-chuck.net/opengeo"

#while True: 
   # address = input("Enter Location: ")
    #if len(address < 1: break):
    #
   # address = address.strip()
   # parms = dict()
   # parms['q'] = address
   # url = serviceurl + urllib.parse.urlencode(parms)

   # print("retrieving", url)
   # uh = urllib.request.urlopen(url, context=ctx)
   # data = uh.read().decode()
   # print("retrieved", len(data), "characters:", data[:20].replace('\n', ' '))

   # js = json.loads(data)
   # lat = js["features"][0]["properties"]["lat"]
   # print("lat", lat)
#