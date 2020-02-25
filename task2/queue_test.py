# import pytest
from tweepy_get import tweepy_get
from image2video import image_to_video
from queue_sys import queue_1
import multiprocessing
import time
import threading
import queue
import os

def test_twitter_get():
  assert os.path.exists('img/BU_Tweets1.png') == True
  assert os.path.exists('img/BostonDynamics11.png') == True
  assert os.path.exists('img/BostonDynamics111.png') == False
  assert os.path.exists('img/realDonaldTrump12.png') == False
  print("Twitter get is passed")
  
def test_image2video():
  assert os.path.exists('BU_ece.avi') == True
  assert os.path.exists('BostonDynamics.avi') == True
  assert os.path.exists('realDonaldTrump.avi') == False
  assert os.path.exists('WHO.avi') == True
  print("Image to video is passed")

def test_queue():
  assert os.path.exists('BU_Tweets.avi') == True
  assert os.path.exists('BU_ece.avi') == True
  assert os.path.exists('BostonDynamics.avi') == True
  assert os.path.exists('WHO.avi') == True
  assert os.path.exists('TIME.avi') == True
  assert os.path.exists('celtics.avi') == True
  assert os.path.exists('nytimes.avi') == True
  assert os.path.exists('washingtonpost.avi') == True
  assert os.path.exists('BillGates.avi') == True
  assert os.path.exists('realDonaldTrump.avi') == False
  print("Queue is passed")

def no_keys():
  if os.path.exists('keys') == False :
    queue_1(keyNames, number_thread)
    assert os.path.exists('BU_Tweets.avi') == True
    assert os.path.exists('BU_ece.avi') == True
    assert os.path.exists('BostonDynamics.avi') == True
    assert os.path.exists('WHO.avi') == True
    assert os.path.exists('TIME.avi') == True
    assert os.path.exists('celtics.avi') == True
    assert os.path.exists('nytimes.avi') == True
    assert os.path.exists('washingtonpost.avi') == True
    assert os.path.exists('BillGates.avi') == True
    assert os.path.exists('realDonaldTrump.avi') == False
    print("No keys test is passed")


keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'BBCWorld', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
number_thread = 4
queue_1(keyNames, number_thread)
test_twitter_get()
test_queue()
test_image2video()
no_keys()




