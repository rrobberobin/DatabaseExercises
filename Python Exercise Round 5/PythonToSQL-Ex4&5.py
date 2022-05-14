
# Exercise 4

import sqlite3
conn = sqlite3.connect('musicalbums.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Albums (
albumName TEXT,
companyName TEXT REFERENCES Companies(companyName),
year INTEGER,
length INTEGER,
genre TEXT CHECK (genre IN ('pop', 'rock', 'jazz', 'classical', 'folk')),
PRIMARY KEY (albumName, companyName)
);""")

cursor.execute("""CREATE TABLE Companies(
companyName TEXT PRIMARY KEY,
country TEXT DEFAULT 'USA',
webpage TEXT NOT NULL
);""")

cursor.execute("""CREATE TABLE Artists (
artistName TEXT PRIMARY KEY,
gender TEXT CHECK (gender IN ('M', 'F', 'O')),
born INTEGER
);""")

cursor.execute("""CREATE TABLE Tracks(
trackNo INTEGER NOT NULL CHECK (trackNo > 0 and trackNo < 100),
albumName TEXT NOT NULL,
companyName TEXT NOT NULL,
trackName TEXT,
artistName TEXT NOT NULL REFERENCES Artists (artistName),
composer TEXT,
lyricist TEXT,
length INTEGER,
FOREIGN KEY (albumName,companyName) REFERENCES Albums (albumName,companyName)
);""")

cursor.execute("INSERT INTO Artists VALUES ('Xzibit','M', 1974);")
cursor.execute("SELECT born FROM Artists WHERE artistName='Xzibit';")
print(cursor.fetchone()[0])
print("\n")

# Exercise 5

for n in range(3):
    name = input("Write the name of company number " + str(n + 1) + " ")
    country = input("In which country is the company resided? ")
    webpage = input("What is the address of the company's webpage? ")
    cursor.execute("INSERT INTO Companies VALUES(?,?,?);", (name, country, webpage))
    print("\n")

for n in range(6):
    name = input("Write the name of album number " + str(n + 1) + " ")
    companyName = input("Which company published the album? ")
    year = input("In what year was the album was published? ")
    length = input("What is the length of the album (in seconds)? ")
    genre = input("What is the genre of the album? ")
    cursor.execute("INSERT INTO Albums VALUES(?,?,?,?,?);", (name, companyName, year, length, genre))
    print("\n")

printAlbums = input("Give a name of a record company. ")
cursor.execute("SELECT albumName, year, genre FROM Albums WHERE companyName=?;", (printAlbums,))
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
