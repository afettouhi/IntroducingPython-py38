import threading


def do_this(what):
    whoami(what)


def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,
                             args=("I'm function %s" % n,))
        p.start()

import threading, queue
import time


def washer(dishes, dish_queue):
    for dish in dishes:
        print("Washing", dish)
        time.sleep(5)
        dish_queue.put(dish)


def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print("Drying", dish)
        time.sleep(10)
        dish_queue.task_done()


dish_queue = queue.Queue()
for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()

dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()

from gevent import monkey

monkey.patch_socket()

from gevent import monkey

monkey.patch_all()

import socket

socket.gethostbyname('www.crappytaxidermy.com')

socket.gethostbyname_ex('www.crappytaxidermy.com')

socket.getaddrinfo('www.crappytaxidermy.com', 80)

socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET,
                   socket.SOCK_STREAM)

import socket
socket.getservbyname('http')

socket.getservbyport(80)

import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
