import os
import cv2
import numpy as np

def image_to_video(keyword):
	path = 'img/'
	filelist = os.listdir(path)

	fps = 1/3 # three seconds per pic
	size = (1200, 630)

	video = cv2.VideoWriter(keyword + ".avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

	for item in filelist:
		if item.endswith('.png'): 
			item = path + item
			print(item)
			img = cv2.imread(item)
			video.write(img)