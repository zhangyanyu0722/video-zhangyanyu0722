# FFmpeg

## Study the following: [Click here]
- Python processes and subprocesses (https://docs.python.org/3/library/subprocess.html)
- Python Threads (https://docs.python.org/3/library/threading.html)
- Python Threads Versus Processes (https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python)
- Please run and test the code provided in (Python Threads Versus Processes) and compare processes and threads
- Install FFMPEG

## Exercise: FFmpeg: [Click here ^v^]
### Preparation:
- Use FFmpeg to re-encode a video file (MOV, or MP4) to two bitrates:
  -- 720p at 2Mbps and 30fps
  -- 480p at 1Mbps and 30fps
- Using the twitter feed, construct a daily video summarizing a twitter handle day
  -- Convert text into an image in a frame
  -- Do a sequence of all texts and images in chronological order.
  -- Display each video frame for 3 seconds
  
### Task 1:
- Estimate the processing power need to execute such operations on your computer
- Estimate the maximum number of such operations that can run on your system

### Task 2:
- Design a module that can queue and process videos and notify the caller when the videos are ready
- Implement the module
- Include tracking interface to show how many processes are going on and success of each

[Click here]: https://github.com/BUEC500C1/video-zhangyanyu0722/tree/master/ThreadsVSProcesses
[Click here ^v^]: https://github.com/BUEC500C1/video-zhangyanyu0722/tree/master/FFmpeg
