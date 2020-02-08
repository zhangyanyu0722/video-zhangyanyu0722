# Study the following:
- Python processes and subprocesses (https://docs.python.org/3/library/subprocess.html)
- Python Threads (https://docs.python.org/3/library/threading.html)
- Python Threads Versus Processes (https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python)
- Please run and test the code provided in (Python Threads Versus Processes) and compare processes and threads
- Install FFMPEG

## Summary
### Multiprocessing
#### Pros
- Separate memory space
- Code is usually straightforward
- Takes advantage of multiple CPUs & cores
- Avoids GIL limitations for cPython
- Eliminates most needs for synchronization primitives unless if you use shared memory (instead, it's more of a communication model for IPC)
- Child processes are interruptible/killable
- Python ```multiprocessing module``` includes useful abstractions with an interface much like ```threading.Thread```
- A must with cPython for CPU-bound processing
#### Cons
- IPC a little more complicated with more overhead (communication model vs. shared memory/objects)
- Larger memory footprint

### Threading
#### Pros
- Lightweight - low memory footprint
- Shared memory - makes access to state from another context easier
- Allows you to easily make responsive UIs
- cPython C extension modules that properly release the GIL will run in parallel
- Great option for I/O-bound applications
#### Cons
- cPython - subject to the GIL
- Not interruptible/killable
- If not following a command queue/message pump model (using the Queue module), then manual use of synchronization primitives become a necessity (decisions are needed for the granularity of locking)
- Code is usually harder to understand and to get right - the potential for race conditions increases dramatically



