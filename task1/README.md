# FFmpeg

## Task 1:
- Estimate the processing power need to execute such operations on your computer
- Estimate the maximum number of such operations that can run on your system

## Preparation:
- For my MAC, the CPU is Intel Core i5 with 2 Cores.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/1.png" width= 400>
</p>
- Then I open the "Activity Monitor" and update the refresh frequency to 1 sec.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/2.png" width= 400>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/3.png" width= 400>
</p>
- Also, I open and surpervise the CPU ussage, CPU history, GPU history.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/5.png" width= 200>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/6.png" width= 200>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/7.png" width= 200>
</p>

## The first test : processing power need to execute FFmpeg in "Activity Monitor"
- Run the command below again, and "Activity Monitor" show max CPU ussage on FFmpeg is about 90%.
```
ffmpeg -i BU_football.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M BU_football_30_720.mp4
```
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/4.png" width= 400>
</p>

## The second test : processing power need to execute FFmpeg in Terminal
- Run ```top``` to monitor all processes, showing as below :
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/8.png" width= 400>
</p>

- Then Run ``` top pid 1797``` to monitor the CPU% during PID 1797
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/9.png" width= 400>
</p>

## Solution
- My MAC has one Dual-core four-thread CPU. It means it might be able to process a maximum of 4 threads per core. So a 2-core CPU with multi-threading of 4 means it can possibly process a maximum of 8 threads or routines at the same time. 2 cores multiplied by 4 threads per core equals a maximum of 8 possible total threads or routines or tasks this CPU can handle simultaneously.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task1/img/5.png" width= 200>
</p>
So the CPU ussage has 4 columns.

- During run the FFmpeg command, the total CPU% reach 90%. But from the CPU ussage columns, we can easily see the first and third threads only use about 40%. It means the Dual-core four-thread CPU has total 200% CPU ussages.

- Maximum number of FFmpeg operations that can run on your system at the same time is 2.















