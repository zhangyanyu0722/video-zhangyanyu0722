# !usr/bin/bash
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# Resource : https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats
# HW4 : Use FFmpeg to re-encode a video file (MOV, or MP4) to two bitrates:
#       720p at 2Mbps and 30fps
#       480p at 1Mbps and 30fps
# =================================================================================== 

ffmpeg -i BU_football.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M BU_football_30_720.mp4
ffmpeg -i BU_football.mp4 -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M BU_football_30_480.mp4