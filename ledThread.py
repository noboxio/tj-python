"""
Author: Brian McGinnis and Patrick McGinnis
"""

import time
from neopixel import *
import threading
import led


class LedThread(threading.Thread):

    def __init__(self, led):
        self.led = led
        self.thread = None
        
            
    def strobe(self):
        self.__clearThread__()
        self.thread = threading.Thread(target = self.led.strobe)
        self.thread.start()
                
    def wheel(self,pos):
        self.__clearThread__()
        self.thred = threading.Thread(target = self.led.wheel, kwargs={'pos':pos})
        self.thread.start()
        
    def customColor(self, r, g, b):
        self.__clearThread__()
        self.thread = threading.Thread(target = self.led.customColor, kwargs={'r':r,'g':g,'b':b})
        self.thread.start()
        
    def __clearThread__(self):
        if self.thread != None:
            self.thread.cancel()
            
    def stop(self):
        self.__clearThread__()


"""

l = LedThread("ID", "NAME")
l.daemon = True
l.start()

print("sleeping")
time.sleep(5)
print("dome sleepoing")
l.changename("hey hey")
print("name changed")


print("sleeping again")
time.sleep(5)
"""
