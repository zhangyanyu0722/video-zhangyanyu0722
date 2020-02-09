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
[Click Here To Get the Detail]
- Convert text into an image in a frame
- Do a sequence of all texts and images in chronological order.
- Display each video frame for 3 seconds

### To review the Video, [CLICK]

[here]: https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats
[Click Here To Get the Detail]: https://github.com/BUEC500C1/video-zhangyanyu0722/tree/master/FFmpeg/Twitter_feed
[CLICK]: https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/FFmpeg/Twitter_feed/twitter.avi
