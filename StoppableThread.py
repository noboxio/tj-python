#!/usr/bin/env python

import threading

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    
    
    



from multiprocessing import Process







def boo():
    while True:
        print("hi")
        time.sleep(2)
        
        
pt
    proc.start()
    time.sleep(2.5)
    proc.terminate()