import sqlite3

# https://www.sqlite.org/lang_select.html
#mbox-short.txt
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname)< 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh: 
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    # opening a set of records with .execute, reads like a file. 
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email,)) # ? is a place holder and doesn't allow sql injection, (email,) = tuple in Python syntax
    row = cur.fetchone() # fetches first one, information from database to make sure there is info there. 
    if row is None: 
        # 1 is initial count, tuple that gives to execute statement coresponding strings/integers 
        cur.execute('''INSERT INTO Counts (email, count) VALUES(?, 1)''', (email,)) 
    else: 
        # adding 1 to the count to go to next email in list.
        cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?', (email,))
    conn.commit() # db is keeping info in memory and needs to write to disk, this will commit every time through the loop. 

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()