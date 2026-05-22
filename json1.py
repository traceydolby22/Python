import json, ssl
import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), 'characters')
print(f"debug: '{data}'")

info = json.loads(data)
print("Total Count:", len(info["comments"]))
#print(json.dumps(info["comments"], indent=4))
sum_of_count = 0 
for item in info["comments"]: 
    sum_of_count += item["count"]
print(sum_of_count)
#data = '''
#{
 # "name" : "Tracey",
 #   "id" : "001",
  #  "x" : "2",
  #  "gender" : "female",
  #  },
 # "address" : {
   # "street" : "1887 street avenue",
   # "city" : "Los Angeles",
   # "state" : "CA",
   # "postalcode" : "90025"
  #},
  ##"phone" : {
   # "type" : "intl",
  #  "number" : "+1 520 472 2615"
 # },
 # "email" : {
  #  "hide" : "no"
 # }
#}'''

#data2 = '''
 #[
 # { "name" : "Tracey", "id" : "001", "x" : "2", "gender" : "female" },
 # { "name" : "Brian", "id" : "002", "x" : "7", "gender" : "male" },
 # { "name" : "Sarah", "id" : "003", "x" : "5", "gender" : "female" }
#]
#'''

#info1 = json.loads(data)
#print("Name: ", info1["name"])
#print("Phone: ", info1["phone"]["number"])
#print("Email: ", info1["email"]["hide"])
#print("City: ", info1["address"]["city"])

#info2 = json.loads(data2)
#for item in info2:
   # print("ID: ", item["id"])
   # print("Attribute: ", item["x"])
   # print("gender: ", item["gender"])