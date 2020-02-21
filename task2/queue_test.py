# import pytest
from tweepy_get import tweepy_get
from image2video import image_to_video
from queue_sys import queue_1
import multiprocessing
import time
import threading
import queue
import os



def test_queue():

# *****************************************************************************************************
# If you want to test the following part, please input the twitter API KEY in the tweepy_get.py
# *****************************************************************************************************

  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  number_thread = 4
  queue_1(keyNames, number_thread)
  assert os.path.exists('BU_Tweets.avi')
  assert os.path.exists('BU_ece.avi')
  assert os.path.exists('BostonDynamics.avi')
  assert os.path.exists('realDonaldTrump.avi')
  assert os.path.exists('WHO.avi')
  assert os.path.exists('TIME.avi')
  assert os.path.exists('celtics.avi')
  assert os.path.exists('nytimes.avi')
  assert os.path.exists('washingtonpost.avi')
  assert os.path.exists('BillGates.avi')







