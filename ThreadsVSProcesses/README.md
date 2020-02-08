# Study the following:
- Python processes and subprocesses (https://docs.python.org/3/library/subprocess.html)
- Python Threads (https://docs.python.org/3/library/threading.html)
- Python Threads Versus Processes (https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python)
- Please run and test the code provided in (Python Threads Versus Processes) and compare processes and threads
- Install FFMPEG

# Steps and Results
## Run and test the code and compare processes and threads
- First, install Gnuplot (http://macappstore.org/gnuplot/)
```
brew install gnuplot
```

- Second, run ThreadsVSProcesses.py
```
python ThreadsVSProcesses.py CPU_Num
```
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/ThreadsVSProcesses/Picture/1.png" width= 500>
</p>

- Then saved the data in a file named "thread_cpu_bound.dat"
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/ThreadsVSProcesses/Picture/2.png" width= 200>
</p>

- Enter the gnuplot in terminal to enter the envs
```
gnuplot
```
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/ThreadsVSProcesses/Picture/3.png" width= 500>
</p>

- Run "thread_cpu_bound.gnuplot" in the terminal
```
set terminal png size 600, 1200
set style data linespoints
set output 'thread_cpu_bound.tmp.png'
set key autotitle columnhead
set multiplot layout 4,1 title "Python Threads vs Processes with 8 hyperthreads" font ",18"
set title font ",14"

set title 'CPU bound'
set key left top
set xlabel "threads"
set ylabel "time (s)"
plot 'thread_cpu_bound.dat' using 1:2, \
     'thread_cpu_bound.dat' using 1:3

set title 'CPU bound / threads'
set key right center
set yrange [0:*]
plot 'thread_cpu_bound.dat' using 1:($2/$1) title 'CpuThread', \
     'thread_cpu_bound.dat' using 1:($3/$1) title 'CpuProcess'

set title 'Thread / Process ratio'
set ylabel "ratio"
set yrange [0:*]
plot 'thread_cpu_bound.dat' using 1:($2/$3) notitle

set title 'IO bound'
set key default
set ylabel "time (s)"
set yrange[0:2]
plot 'thread_cpu_bound.dat' using 1:4 title 'IoThread', \
     'thread_cpu_bound.dat' using 1:5 title 'IoProcess'
```
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/ThreadsVSProcesses/Picture/4.png" width= 500>
</p>
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/ThreadsVSProcesses/Picture/5.png" width= 500>
</p>

- Exit the gnuplot envs and will see the .png file
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/ThreadsVSProcesses/thread_cpu_bound.tmp.png" width= 500>
</p>

### Conclusions from the picture above :
- For CPU bound work, multiprocessing is always faster, presumably due to the GIL
- For IO bound work. both are exactly the same speed
- Threads only scale up to about 4x instead of the expected 8x since I'm on an 8 hyperthread machine.

## Install FFMPEG
- To install the FFmpeg easily
```
brew install ffmpeg
```

# Summary
## Multiprocessing
### Pros
- Separate memory space
- Code is usually straightforward
- Takes advantage of multiple CPUs & cores
- Avoids GIL limitations for cPython
- Eliminates most needs for synchronization primitives unless if you use shared memory (instead, it's more of a communication model for IPC)
- Child processes are interruptible/killable
- Python ```multiprocessing module``` includes useful abstractions with an interface much like ```threading.Thread```
- A must with cPython for CPU-bound processing
### Cons
- IPC a little more complicated with more overhead (communication model vs. shared memory/objects)
- Larger memory footprint

## Threading
### Pros
- Lightweight - low memory footprint
- Shared memory - makes access to state from another context easier
- Allows you to easily make responsive UIs
- cPython C extension modules that properly release the GIL will run in parallel
- Great option for I/O-bound applications
### Cons
- cPython - subject to the GIL
- Not interruptible/killable
- If not following a command queue/message pump model (using the Queue module), then manual use of synchronization primitives become a necessity (decisions are needed for the granularity of locking)
- Code is usually harder to understand and to get right - the potential for race conditions increases dramatically



