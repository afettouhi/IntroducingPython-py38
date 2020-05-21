poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
len(poem)

fout = open('relativity', 'wt')
fout.write(poem)

fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset + chunk])
    offset += chunk

fout.close()

# fout = open('relativity', 'xt')

try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close()
len(poem)

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines:
    print(line, end='')

bdata = bytes(range(0, 256))
len(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)

fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset + chunk])
    offset += chunk

fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)

fin.close()

with open('relativity', 'wt') as fout:
    fout.write(poem)

fin = open('bfile', 'rb')
fin.tell()

fin.seek(255)

bdata = fin.read()
len(bdata)

bdata[0]

import os

os.SEEK_SET

os.SEEK_CUR

os.SEEK_END

fin = open('bfile', 'rb')

fin.seek(-1, 2)

fin.tell()

bdata = fin.read()
len(bdata)

bdata[0]

fin = open('bfile', 'rb')

fin.seek(254, 0)

fin.tell()

fin.seek(1, 1)

fin.tell()

bdata = fin.read()
len(bdata)

bdata[0]

import csv

villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]
with open('villains', 'wt') as fout:  # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv

with open('villains', 'rt') as fin:  # context manager
    cin = csv.reader(fin)
    villains = [row for row in cin]  # This uses a list comprehension

print(villains)

import csv

with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

import csv

villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

import csv

with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)

import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

len(root)  # number of menu sections

len(root[0])  # number of breakfast items

menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

import json

menu_json = json.dumps(menu)
menu_json

menu2 = json.loads(menu_json)
menu2

import datetime

now = datetime.datetime.utcnow()
now
datetime.datetime(2013, 2, 22, 3, 49, 27, 483336)
# json.dumps(now)

now_str = str(now)
json.dumps(now_str)

from time import mktime

now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)

from time import mktime
now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance() checks the type of obj
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # else it's something the normal decoder knows:
        return json.JSONEncoder.default(self, obj)


json.dumps(now, cls=DTEncoder)

type(now)

isinstance(now, datetime.datetime)

type(234)

isinstance(234, int)

type('hey')

isinstance('hey', str)

import yaml

with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.load(text)
data['details']

len(data['poems'])

data['poems'][1]['title']

# insecure:
from xml.etree.ElementTree import parse

# et = parse(xmlfile)
# protected:
from defusedxml.ElementTree import parse

import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

cfg

cfg['french']

cfg['french']['greeting']

cfg['files']['bin']

import pickle
import datetime

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
now1

now2

import pickle


class Tiny():
    def __str__(self):
        return 'tiny'


obj1 = Tiny()
obj1

str(obj1)

pickled = pickle.dumps(obj1)
pickled

obj2 = pickle.loads(pickled)
obj2

str(obj2)

import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)''')

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')

curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

curs.execute('SELECT * FROM zoo')

rows = curs.fetchall()
print(rows)

curs.execute('SELECT * from zoo ORDER BY count')

curs.fetchall()

curs.execute('SELECT * from zoo ORDER BY count DESC')

curs.fetchall()

curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')

curs.fetchall()

curs.close()
conn.close()

import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)''')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)

conn.execute(ins, 'bear', 2, 1000.0)

conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo')

print(rows)

for row in rows:
    print(row)

import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
               )
meta.create_all(conn)

conn.execute(zoo.insert(('bear', 2, 1000.0)))

conn.execute(zoo.insert(('weasel', 1, 2000.0)))

conn.execute(zoo.insert(('duck', 10, 0)))

result = conn.execute(zoo.select())

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('sqlite:///zoo.db')

Base = declarative_base()


class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)


Base.metadata.create_all(conn)

first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
first

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

session.add(first)
session.add_all([second, third])

session.commit()

import dbm
db = dbm.open('definitions', 'c')

db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

len(db)

db['pesto']

db.close()
db = dbm.open('definitions', 'r')
db['mustard']

import memcache
db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')

db.get('marco')

db.set('ducks', 0)

db.get('ducks')

db.incr('ducks', 2)

db.get('ducks')

import redis
conn = redis.Redis()

conn.keys('*')

conn.set('secret', 'ni!')

conn.set('carats', 24)

conn.set('fever', '101.5')

conn.get('secret')

conn.get('carats')

conn.get('fever')

conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')

conn.get('secret')

conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')

conn.get('secret')

conn.getrange('secret', -6, -1)

conn.setrange('secret', 0, 'ICKY')

conn.get('secret')

conn.mset({'pie': 'cherry', 'cordial': 'sherry'})

conn.mget(['fever', 'carats'])

conn.delete('fever')

conn.incr('carats')

conn.incr('carats', 10)

conn.decr('carats')

conn.decr('carats', 15)

conn.set('fever', '101.5')

conn.incrbyfloat('fever')

conn.incrbyfloat('fever', 0.5)

conn.incrbyfloat('fever', -2.0)

conn.lpush('zoo', 'bear')

conn.lpush('zoo', 'alligator', 'duck')

conn.linsert('zoo', 'before', 'bear', 'beaver')

conn.linsert('zoo', 'after', 'bear', 'cassowary')

conn.lset('zoo', 2, 'marmoset')

conn.rpush('zoo', 'yak')

conn.lindex('zoo', 3)

conn.lrange('zoo', 0, 2)

conn.ltrim('zoo', 1, 4)

conn.lrange('zoo', 0, -1)

conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})

conn.hset('song', 'mi', 'a note to follow re')

conn.hget('song', 'mi')

conn.hmget('song', 're', 'do')

conn.hkeys('song')

conn.hvals('song')

conn.hlen('song')

conn.hgetall('song')

conn.hsetnx('song', 'fa', 'a note that rhymes with la')

conn.sadd('zoo', 'duck', 'goat', 'turkey')

conn.scard('zoo')

conn.smembers('zoo')

conn.srem('zoo', 'turkey')

conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')

conn.sinter('zoo', 'better_zoo')

conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo')

conn.smembers('fowl_zoo')

conn.sunion('zoo', 'better_zoo')

conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo')

conn.smembers('fabulous_zoo')

conn.sdiff('zoo', 'better_zoo')

conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo')

conn.smembers('zoo_sale')

import time
now = time.time()
now

conn.zadd('logins', 'smeagol', now)

conn.zadd('logins', 'sauron', now+(5*60))

conn.zadd('logins', 'bilbo', now+(2*60*60))

conn.zadd('logins', 'treebeard', now+(24*60*60))

conn.zrank('logins', 'bilbo')

conn.zscore('logins', 'bilbo')

conn.zrange('logins', 0, -1)

conn.zrange('logins', 0, -1, withscores=True)

days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

conn.setbit(days[0], big_spender, 1)

conn.setbit(days[0], tire_kicker, 1)

conn.setbit(days[1], big_spender, 1)

conn.setbit(days[2], big_spender, 1)

conn.setbit(days[2], late_joiner, 1)

for day in days:
    conn.bitcount(day)

conn.getbit(days[1], tire_kicker)

conn.bitop('and', 'everyday', *days)

conn.bitcount('everyday')

conn.getbit('everyday', big_spender)

conn.bitop('or', 'alldays', *days)

conn.bitcount('alldays')

import time
key = 'now you see it'
conn.set(key, 'but not for long')

conn.expire(key, 5)

conn.ttl(key)

conn.get(key)

time.sleep(6)
conn.get(key)
