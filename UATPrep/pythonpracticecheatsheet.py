# Key exists?
if "key" not in dict:
   print("key")
# Value is non-empty string?
if len(dict["key"]) == 0:
    print("key")
# Value is correct type?
if not isinstance(dict["key"], int):
    print("key")
# Value meets a condition?
if dict["key"] < 0:
    print("key")
# Loop passes ONE item
for item in items:
    my_function(item)  # not items — item
    print("key")
# Here's the simple rule:

#If you're building a new list by looping through an existing one, it's probably a list comprehension.
eligible_ids = [user["id"] for user in users if is_eligible(user)]
ineligible_ids = [user["id"] for user in users if not is_eligible(user)]
#That's it. Three signals that tell you to reach for one:
#You start with result = []
#You loop with for x in something
#You append at the end — with or without an if condition#

# when you're doing multiple things inside the loop (like appending to two different lists, or doing calculations), stick with the regular loop.