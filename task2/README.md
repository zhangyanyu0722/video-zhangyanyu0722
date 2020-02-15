# FFmpeg

## Task 2: 
- Develop a queue system that can exercise your requirements with stub functions
- Develop the twitter functionality with an API
- Integrate them

## Test
- Run the file ```queue_sys.py```
```
python queue_sys.py
```

## Solution
- In this task, I build a queue and test with 10 twitter users('BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates')
- Get the status of four threads on my MAC, then ```q.put(item)``` for each of them from the queue.
- In the activity monitor, the ussage of four threads are showing below:
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/task2/picture/3.png" width= 200>
</p>


