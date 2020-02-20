import pytest
from tweepy_get import tweepy_get
from image2video import image_to_video
import multiprocessing
import time
import threading
import queue
import os

def worker(q):
  i = 0
  while True:
    item = q.get()
    if item is None:
      print("Break ! Because item is None")
      break
    tweepy_get(item)
    image_to_video(item)
    i += 1
    print("---------------Thread Done--------------")
    q.task_done()

def queue_1(keyNames, number_thread):
  q = queue.Queue()
  threads = []

  for i in range(number_thread):
    t = threading.Thread(target=worker(q))
    t.start()
    threads.append(t)

  for item in keyNames:
    q.put(item)

  q.join()

  for i in range(number_thread):
    q.put(None)

  for t in threads:
    t.join()

def test_queue():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  number_thread = 4
  queue_1(keyNames, number_thread)
  assert os.path.exists('BU_Tweets.avi')






