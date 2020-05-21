import urllib.request as ur
from urllib.parse import quote
import json

title = input('Type a movie title: ')

# needs api keep as of now to work
url = 'http://www.omdbapi.com/?t=%s' % quote(title)
conn = ur.urlopen(url)

print(conn.status)

data = conn.read()
print(data)

print(conn.getheader('Content-Type'))

try:
    str_data = data.decode('utf8')
    js_data = json.loads(str_data)
    print('title:', js_data['Title'])
    print('plot:', js_data['Plot'])
except:
    print('Sorry, no match for', title)

for key, value in conn.getheaders():
    print(key, value)

import requests
import json

url = 'http://www.omdbapi.com'
title = input('Type a movie title: ')

args = {'t': title}
resp = requests.get(url, params=args)
resp

js_data = resp.json()
try:
    print('title:', js_data['Title'])
    print('plot:', js_data['Plot'])
except:
    print('Sorry, no match for', title)

import bottle

application = bottle.default_app()


@bottle.route('/')
def home():
    return "apache and wsgi, sitting in a tree"


import antigravity

import webbrowser

url = 'http://www.python.org/'
webbrowser.open(url)

webbrowser.open_new(url)

webbrowser.open_new_tab('http://www.python.org/')
