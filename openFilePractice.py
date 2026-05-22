openingfile = open("mbox-short.txt")
counts = dict()
for line in openingfile: 
    lines = line.rstrip()
    if not lines.startswith("From: "): continue
    words = lines.split()
    #if len(words) < 3 or words[0] != "From: ": continue
    
    emails = words[1]
    counts[emails] = counts.get(emails, 0) + 1
    
    emailcount = None
    emailOffender = None
    for email, count in counts.items():  
        if emailcount is None or count > emailcount:
            emailOffender = email
            emailcount = count
print(emailOffender, emailcount)



#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "intro.txt"
fhand = open("info.txt")

for line in fhand:
    lines = line.rstrip()
    if lines.startswith("Subject:") :
        print(lines)
print(line)

# find top 5 words by frequency in a file
#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "clown.txt"

#fhand = open(fname)
#many = dict()
#for line in fhand:
#    words = line.split()
 #   for word in words:
   ##     many[word] = many.get(word, 0) + 1
#print(many.items()) #gives key value pairs in a tuple
#temp = dict()
#newlst = list()
#for key, value in many.items():
 #   tup = (value,key)
 #   newlst.append(tup)
#cool = sorted(newlst, reverse=True)
#for v,k in cool[:5] :
 #   print(k,v)


def romanToInt(self, s: str) -> int:
    romanNumerals = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000}
    numbers = list()
    sum = 0
    for strings in s: 
        if s == "I" or "V" or "X" or "L" or "C" or "D" or "M":
            numbers.append(strings)
    for i in range(len(numbers)-1):
        # need to compare 1 val with next and if it's < number assigned it's a subtraction of that number..
        # right now it's not registering 1 character, with 2 it finally has correct num.    
        if numbers[i] >= numbers[i+1]:
            sum += romanNumerals[numbers[i]] 
        elif numbers[i] == numbers[i+1]:   
            sum += romanNumerals[numbers[i]] 
        else:
            sum -= romanNumerals[numbers[i]] 
        print(sum)

romanToInt("C", "MCMXCIV")