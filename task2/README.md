# FFmpeg

## Task 2: 
- Develop a queue system that can exercise your requirements with stub functions
- Develop the twitter functionality with an API
- Integrate them

## Test
- Run the command below to access .sh and run it
```
chmod 777 ffmpeg_queue.sh
```
```
ffmpeg_queue.sh
```
- The results are showing below, it occupies about 12% CPU
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/11.png" width= 400>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/22.png" width= 400>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/33.png" width= 400>
</p>

- If run set 4 videos' transforation at the same time. We can see 360% CPU ussage
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/1.png" width= 400>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/2.png" width= 400>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/3.png" width= 400>
</p>

- From the terminal, use ```top```to surpervise the CPU ussage:

<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/5.png" width= 400>
</p>

- After terminate the task, CPU ussage decrease to nearly 0%
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/img/4.png" width= 400>
</p>

