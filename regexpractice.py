import re
def add_nums():
    open_file = open("regexSum.txt")
    numlist = list()
    for line in open_file:
        line = line.rstrip()
        stuff = re.findall("[0-9]+", line)
        if len(stuff) == 0 : continue
        for num in stuff:
            numlist.append(int(num))
    print(sum(numlist))     
add_nums()

def count_ands() :
    open_file = open("regexSum.txt")
    count = 0
    for lines in open_file:
        lines = lines.rstrip()
        if re.search("\sand\s+", lines) :
            count = count + 1
    print(count)
count_ands()