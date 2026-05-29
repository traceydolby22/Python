import urllib.request, urllib.parse, urllib.error
import http, sqlite3, json, time, ssl, sys

serviceurl = "https://py4e-data.dr-chuck.net/opengeo?"

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open('where.data')
count = 0 
nofound = 0

for line in fh: 
    if count > 100: 
        print("retrieved 100 locations, restart to retrieve more")
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address = ?", (memoryview(address.encode()),))

    try: 
        data = cur.fetchone()[0]
        print("found in database", address)
        continue
    except: 
        pass
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print("retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("retrieved", len(data), "characters", data[:20].replace("\n", " "))
    count = count + 1 

    try: 
        js = json.loads(data)
    except: 
        print(data)
        continue
# sanity checks 
    if not js or "features" not in js:
        print("==== Download Error ====")
        print(data)
        break

    if len(js["features"]) == 0:
        print("===Object not found ===")
        nofound = nofound + 1

    cur.execute(''' INSERT INTO Locations ( address, geodata) VALUES (?,?)''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()

    if count % 10 == 0: 
        print("pausing for a bit")
        time.sleep(5)

if nofound > 0: 
    print("Number of features for which the location could not be found", nofound)

print("run geodump.py to read the data from database so you can vizualize it on the map")