#Database contains many tables. Relation (or table) contain tuples / attributes.
#Tuple or rwo is a set of fields that represents an "object"
#Attribute or columns are elements of data corresponding to the "object"
#A relation is a set of tuples that have the same attributes. The metadata in the first row is the schema.
#SQL is the API between the application and the databases
import sqlite3
def worked_example():
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor() #cursor is like a handle
    cur.execute('DROP TABLE IF EXISTS Counts') #checks if table exists
    cur.execute('''
    CREATE TABLE Counts (email TEXT, count INTEGER)''')

    fname = input('Enter file name: ')
    if (len(fname) < 1): fname = 'mbox-short.txt'
    fh = open(fname)
    for line in fh:
        if not line.startswith('From'): continue #we only get the 'From:' lines
        pieces = line.split()
        email = pieces[1] #selects the second part of the 'From:' lines
        cur.execute('SELECT count FROM Counts WHERE email = ?', (email,)) #? is a placeholder which will be replaced by email. (email,) is a tuple.
        row = cur.fetchone() #grabs the first row and inserts into row
        if row is None:
            cur.execute('''INSERT INTO Counts (email, count)
            VALUES (?,1)''', (email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
        conn.commit() #commits to the disk - runs slow and can be done fewer times

    #https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()
#worked_example()

def database_assignment():
    conn = sqlite3.connect('assignment2.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Counts')
    cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

    fname = input('Enter file name: ')
    if (len(fname)<1): fname = 'mbox.txt'
    fh = open(fname)
    for line in fh:
        if not line.startswith('From:'): continue
        pieces = line.split('@')
        org = pieces[1]
        cur.execute('SELECT count FROM Counts WHERE org =?',(org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''
            INSERT INTO Counts (org, count) 
            VALUES (?,1)''',(org,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org =?',(org,))
    conn.commit()

    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])
    cur.close()

database_assignment()

