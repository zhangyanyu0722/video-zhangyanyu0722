import os
import cv2
import numpy as np

path = 'result/'
filelist = os.listdir(path)

fps = 1/3 # three mins per pic
size = (1338, 678) 

video = cv2.VideoWriter("twitter.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

for item in filelist:
    if item.endswith('.png'): 
        item = path + item
        print(item)
        img = cv2.imread(item)
        video.write(img)
