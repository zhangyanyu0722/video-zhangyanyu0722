# !usr/bin/bash
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW4 : Use FFmpeg to queue and process videos:
# =================================================================================== 
for i in *.mp4; do ffmpeg -i "$i" -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M 2/"${i%.*}_2.mp4"; done
python finish.py





