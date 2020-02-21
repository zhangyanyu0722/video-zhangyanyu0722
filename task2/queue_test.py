# import pytest
from tweepy_get import tweepy_get
from image2video import image_to_video
from queue_sys import queue_1
import multiprocessing
import time
import threading
import queue
import os
# *****************************************************************************************************
# If you want to test the following part, please input the twitter API KEY in the key.txt
# *****************************************************************************************************
def test_twitter_get():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  for key in keyNames:
#     pass # delate this line
    tweepy_get(key)
#   assert os.path.exists('img/BU_Tweets1.png') == True
#   assert os.path.exists('img/BostonDynamics11.png') == True
#   assert os.path.exists('img/realDonaldTrump12.png') == True
  
def test_image2video():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  for key in keyNames:
    pass # delate this line
#     image_to_video(key)
#   assert os.path.exists('BU_ece.avi') == True
#   assert os.path.exists('BostonDynamics.avi') == True
#   assert os.path.exists('realDonaldTrump.avi') == True
#   assert os.path.exists('WHO.avi') == True
    
def test_queue():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  number_thread = 4
#   queue_1(keyNames, number_thread)
#   assert os.path.exists('BU_Tweets.avi') == True
#   assert os.path.exists('BU_ece.avi') == True
#   assert os.path.exists('BostonDynamics.avi') == True
#   assert os.path.exists('realDonaldTrump.avi') == True
#   assert os.path.exists('WHO.avi') == True
#   assert os.path.exists('TIME.avi') == True
#   assert os.path.exists('celtics.avi') == True
#   assert os.path.exists('nytimes.avi') == True
#   assert os.path.exists('washingtonpost.avi') == True
#   assert os.path.exists('BillGates.avi') == True







