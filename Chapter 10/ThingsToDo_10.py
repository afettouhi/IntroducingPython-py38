# 10.1
from datetime import date

fout = open('today.txt', 'w')
today = date.today()
fout.write(str(today))
fout.close()

# 10.2
with open('today.txt')as fin:
    today_string = fin.read()
    print(today_string)

# 10.3
import time

fmt = "%Y-%m-%d"
time.strptime(today_string, fmt)

# 10.4
import os

os.listdir('.')

# 10.5
import os

os.listdir('..')

# 10.6
import multiprocessing
from datetime import datetime
from time import sleep
import random


def now(seconds):
    sleep(seconds)
    print("wait", seconds, " seconds", "time is ", datetime.now())


if __name__ == "__main__":
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()

# 10.7
BD = date(1976, 10, 14)

# 10.8
BD.weekday()

# 10.9
from datetime import timedelta
party_day = BD + timedelta(days=10000)
print(party_day)
