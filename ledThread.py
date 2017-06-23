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
        
            
    def strobe(self):
        strobeThread = threading.Thread(target = self.led.strobe)
        strobeThread.start()
                
    def wheel(self,pos):
        wheelThread = threading.Thread(target = self.led.wheel, kwargs={'pos':pos})
        wheelThread.start()
        
    def customColor(self, r, g, b):
        customColorThread = threading.Thread(target = self.led.customColor, kwargs={'r':r,'g':g,'b':b})
        customColorThread.start()


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
