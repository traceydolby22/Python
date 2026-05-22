import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

from flask import ctx
from bs4 import BeautifulSoup

data = '''
<person>
  <name>Tracey</name>
  <phone type="intl">
    +1 520 472 2615
  </phone>
  <email hide="no"/>
</person>'''

data1 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Tracey</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Chuck</name>
        </user>
    </users>  
</stuff>  
'''
tree = ET.fromstring(data)
print("Name: " , tree.find("name").text)
print("Phone: " , tree.find("phone").text)
print("Email: " , tree.find("email").get("hide"))

tree = ET.fromstring(data1)
lst = tree.findall("users/user")
print("User count:", len(lst))
for item in lst:
    print("ID: ", item.find("id").text)
    print("Name: " , item.find("name").text)
    print("Attribute: " , item.get("x"))


#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 


file = input("Enter file name: ")
html = urllib.request.urlopen(file, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")

tree = ET.fromstring(html)
lst = tree.findall("users/user")
counts = tree.findall(".//count")

for count in counts:
    sumnums = sum(int(count.text) for count in counts)
print(sumnums)
