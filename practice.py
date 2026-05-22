x = 22
if x < 10:
    print("smaller")
if x > 20: 
    print("bigger")

#print("finish")

def greet(): 
    return "hello"
#print(greet(), "Tracey")
big = max("Hello world") # max is magic Python function that returns the largest item in an iterable


url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
#def process_google_doc(doc_url):
   # print(f"Received Google Doc URL: {doc_url}")

#process_google_doc(url)

largest_so_far = -1
#print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
   # print(largest_so_far, the_num)
#print("After", largest_so_far)

count = 0 
sum = 0 
#print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
#print("After", count, sum, sum/count)

largest_so_far = -1
#print("before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
#print("after", largest_so_far)

smallest_so_far = None
#print("before")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    #print(smallest_so_far, value)
#print("after", smallest_so_far)
#print(len("banana") * 7)
x = 'From marquard@uct.ac.za'
#print(x[14:17])
#greet = "Hello Bob"
#print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
#print(data[pos:pos+3])

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#print("how old are you?", end = ' ')
#age = input() # this prompts user for input in console.. could create a game using this
#height = input("how tall are you? " )
#weight = input("How much do you weigh? " )
#print(f"so, you're {age} years old, {height} ft. tall and {weight} lbs." )

def look_for_key(main_box_):
    pile = main_box.make_a_pile_to_look_throuhgh()
    while pile is not empty: 
        box = pile.graba_a_box()
        for item in box: 
            if item.is_a_box():
                look_for_key(item)
            elif item.is_a_key():
                print("found the key!")

#recursion is when a function calls itself, it can be used to solve problems that can be broken down into smaller, similar problems. In the example above, the function look_for_key is calling itself to look through nested boxes until it finds the key.

#def look_for_key(box):
 #   for item in box: 
 #       if item.is_a)box():
  #          look_for_key(item)
   #     elif item.is_a_key():
    #        print("found the key!")
#print(look_for_key(box))

def countdown(i): 
    print(i)
    if i <= 0:
        return
    else: 
        countdown(i-1)
print(countdown(2))

def greet(name) :
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

greet("Tracey")

#recursive function:
def fact(x):
    if x == 1: 
        return 1
    else:
        print(x)
        return x * fact(x-1)
print(fact(4))

def quicksort(arr):
    if len(arr) < 2: 
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([15, 10] + [33] + quicksort([])))