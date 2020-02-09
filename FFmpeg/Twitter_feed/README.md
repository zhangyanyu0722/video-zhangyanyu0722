# FFmpeg
## Steps and results:
### Use FFmpeg to re-encode a video file (MOV, or MP4) to two bitrates:
- 720p at 2Mbps and 30fps
```
ffmpeg -i BU_football.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M BU_football_30_720.mp4
```
- 480p at 1Mbps and 30fps
```
ffmpeg -i BU_football.mp4 -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M BU_football_30_480.mp4
```
- For more infomation, view [here]
### Using the twitter feed, construct a daily video summarizing a twitter handle day
- Convert text into an image in a frame
- Do a sequence of all texts and images in chronological order.
- Display each video frame for 3 seconds
  
## Task 1:
- Estimate the processing power need to execute such operations on your computer
- Estimate the maximum number of such operations that can run on your system

## Task 2:
- Design a module that can queue and process videos and notify the caller when the videos are ready
- Implement the module
- Include tracking interface to show how many processes are going on and success of each

[here]: https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats
