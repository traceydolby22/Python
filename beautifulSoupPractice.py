import html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

url = input("Enter url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#/* n = 0
#count = 0

#numbers = input("Enter count: ")
#position = input("Enter position: ")
#while n < int(numbers): 
   # html = urllib.request.urlopen(url, context=ctx).read()
    #soup = BeautifulSoup(html, "html.parser")
   # tags = soup('a')
    #for tag in tags:
     # count = count +1
     # if count == int(position):
     #   url = tag.get("href", None)
     #   print("Retrieving:", url)
     #   count = 0
     #   break
   # n = n + 1
tags = soup('a')
for tag in tags: 
    print(tag.get("class", None))

    # use https://www.dr-chuck.com/ to test the code.  It has a lot of links in it.
    # use http://py4e-data.dr-chuck.net/known_by_Sonniva.html
  #Look at the parts of a tag
  #print('TAG:',tag)
  #print('URL:',tag.get('comments', None))
  #print('Contents:',tag.contents[0])
  #print('Attrs:',tag.attrs)
tags = soup("span")
counts = list()
total = 0
for tag in tags:
  counts.append(tag.contents[0])
  total = total + 1
incounts = [int(i) for i in counts]

print("Counts:", counts)
print("Total comments:", total)
print("Sum of comment counts:", sum(incounts))
