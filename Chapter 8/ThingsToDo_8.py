# 8.1
test1 = 'This is a test of the emergency text system'

fout = open('test.txt', 'wt')
fout.write(test1)

fout.close()


# 8.2
fin = open('test.txt', 'rt')
test2 = fin.read()
fin.close()

if test1 is test2:
    print("True")
else:
    print("False")

# 8.3 & 8.4
import csv

with open('books.csv', 'rt') as fin:
    book = csv.DictReader(fin, fieldnames=['author', 'book'])
    fout = [row for row in book]

print(fout)

# 8.5 & 8.6
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
    (title VARCHAR(20) PRIMARY KEY,
     author VARCHAR(20),
     year INT)''')

curs.close()
conn.close()

# 8.7
import csv
import sqlite3

with open('books1.csv', 'r') as fin:
    book1 = csv.DictReader(fin)
    book1_db = [(i['title'], i['author'], i['year']) for i in book1]

conn = sqlite3.connect('books1.db')
curs = conn.cursor()
curs.execute("CREATE TABLE t (title, author, year);")
curs.executemany("INSERT INTO t (title, author, year) VALUES (?, ?, ?);", book1_db)

conn.commit()
conn.close()

# 8.8
conn = sqlite3.connect('books1.db')
curs = conn.cursor()
curs.execute('SELECT title FROM t')
rows = curs.fetchall()
print(rows)

conn.commit()
conn.close()

# 8.9
import sqlite3

conn = sqlite3.connect('books1.db')
curs = conn.cursor()
curs.execute('SELECT * FROM t ORDER BY title')
rows = curs.fetchall()
print(rows)

conn.commit()
conn.close()

# 8.10
import sqlalchemy as sa

conn = sa.create_engine('sqlite:////home/af/Dokumenter/Programs/IntroducingPython-py38/Chapter 8/books1.db')

rows = conn.execute('SELECT * FROM t ORDER BY title')

for row in rows:
    print(row)

# 8.11
import redis
conn = redis.Redis('localhost', 6379)

conn.hset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hset('test', 'count', 2)

conn.hgetall('test')

# 8.12
