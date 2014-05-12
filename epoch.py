import datetime, threading, time

next_call = time.time()
current_milli_time = lambda: int(round(time.time()))

def foo():
    global next_call
    print current_milli_time()
    next_call = next_call+1
    threading.Timer( next_call - time.time(), foo ).start()

foo()
