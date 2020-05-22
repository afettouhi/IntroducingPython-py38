fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

import os
os.path.exists('oops.txt')

os.path.exists('./oops.txt')

os.path.exists('waffles')

os.path.exists('.')

os.path.exists('..')

name = 'oops.txt'
os.path.isfile(name)

os.path.isdir(name)

os.path.isdir('.')

os.path.isabs(name)

os.path.isabs('/big/fake/name')

os.path.isabs('big/fake/name/without/a/leading/slash')

import shutil
shutil.copy('oops.txt', 'ohno.txt')

import os
os.rename('ohno.txt', 'ohwell.txt')

os.link('oops.txt', 'yikes.txt')
os.path.isfile('yikes.txt')

os.path.islink('yikes.txt')

os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt')

os.chmod('oops.txt', 0o400)

import stat
os.chmod('oops.txt', stat.S_IRUSR)

uid = 5
gid = 22
#os.chown('oops', uid, gid)

os.path.abspath('oops.txt')

os.path.realpath('jeepers.txt')

os.remove('oops.txt')
os.path.exists('oops.txt')

os.mkdir('poems')
os.path.exists('poems')

os.rmdir('poems')
os.path.exists('poems')

os.mkdir('poems')

os.listdir('poems')

os.mkdir('poems/mcintyre')
os.listdir('poems')

fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')

fout.close()

os.listdir('poems/mcintyre')

import os
os.chdir('poems')
os.listdir('.')

import glob
glob.glob('m*')

glob.glob('??')

glob.glob('m??????e')

glob.glob('[klm]*e')

import os
os.getpid()

os.getcwd()

os.getuid()

os.getgid()

import subprocess
ret = subprocess.getoutput('date')
ret

ret = subprocess.getoutput('date -u')
ret

ret = subprocess.getoutput('date -u | wc')
ret

ret = subprocess.check_output(['date', '-u'])
ret

ret = subprocess.getstatusoutput('date')
ret

ret = subprocess.call('date')

ret

ret = subprocess.call('date -u', shell=True)

ret = subprocess.call(['date', '-u'])

import calendar
calendar.isleap(1900)

calendar.isleap(1996)

calendar.isleap(1999)

calendar.isleap(2000)

calendar.isleap(2002)

calendar.isleap(2004)

from datetime import date
halloween = date(2014, 10, 31)
halloween

halloween.day

halloween.month

halloween.year

halloween.isoformat()

from datetime import date
now = date.today()
now

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
tomorrow

now + 17*one_day

yesterday = now - one_day
yesterday

from datetime import time
noon = time(12, 0, 0)
noon

noon.hour

noon.minute

noon.second

noon.microsecond

from datetime import datetime
some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
some_day

some_day.isoformat()

from datetime import datetime
now = datetime.now()
now

now.month

now.day

now.hour

now.minute

now.second

now.microsecond

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
noon_today

noon_today.date()

noon_today.time()

import time
now = time.time()
now

time.ctime(now)

time.localtime(now)

time.gmtime(now)

tm = time.localtime(now)
time.mktime(tm)

import time
now = time.time()
time.ctime(now)

import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
t

time.strftime(fmt, t)

from datetime import date
some_day = date(2014, 7, 4)
fmt = "It's %B %d, %Y, local time %I:%M:%S%p"
some_day.strftime(fmt)

from datetime import time
some_time = time(10, 35)
some_time.strftime(fmt)

import time
fmt = "%Y-%m-%d"
time.strptime("2012 01 29", fmt)

time.strptime("2012-01-29", fmt)

time.strptime("2012-13-29", fmt)

import locale
from datetime import date
halloween = date(2014, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B %d')

import locale
names = locale.locale_alias.keys()

good_names = [name for name in names if \
len(name) == 5 and name[2] == '_']

good_names[:5]

de = [name for name in good_names if name.startswith('de')]
de