import sqlite3

def example():
    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
        
    CREATE TABLE Artist (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
        );
    CREATE TABLE Album (
        id INTEGER PRIMARY KEY,
        artist_id INTEGER,
        title TEXT UNIQUE
        );
    CREATE TABLE Track (
        id INTEGER PRIMARY KEY,
        title TEXT UNIQUE,
        album_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
        );
    ''')
    handle = open('tracks.csv')

    for line in handle:
        line = line.strip()
        pieces = line.split(',')
        if len(pieces)<6: continue

        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]

        print(name, artist, album, count, rating, length)

        cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        cur.execute(''' INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        cur.execute ('''INSERT OR IGNORE INTO Track 
        (title, album_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?)''', (name, album_id, length, rating, count))
        conn.commit()
#example()

def assignment():
    conn = sqlite3.connect('assignment.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    
    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER, 
        title TEXT UNIQUE
    );
    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')
    # Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
    #   0                          1      2           3  4   5      6
    handle = open('tracks.csv')
    for line in handle:
        line = line.strip()
        pieces = line.split(',')
        if len(pieces)<7: continue
        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]
        genre = pieces[6]
        print(name, artist, album, count, rating, length, genre)
        cur.execute('''INSERT OR IGNORE INTO Artist (name)
                VALUES (?)''', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        cur.execute(''' INSERT OR IGNORE INTO Album (title, artist_id)
                VALUES (?, ?)''', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Genre (name)
            VALUES (?)''', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]
        cur.execute('''INSERT OR IGNORE INTO Track 
                (title, album_id, len, rating, count, genre_id)
                VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, length, rating, count, genre_id))
        conn.commit()
assignment()