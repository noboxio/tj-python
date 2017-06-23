"""
Author: Brian McGinnis and Patrick McGinnis
"""

import time
from neopixel import *
from multiprocessing import Process
import led




class LedProcess():

    def __init__(self, led):
        self.led = led
        self.process = None
        
            
    def strobe(self):
        self.process.terminate()
        self.process = Process(target = self.led.strobe)
        self.process.start()
                
    def wheel(self,pos):
        self.process.terminate()
        self.process = Process(target = self.led.wheel, kwargs={'pos':pos})
        self.process.start()
        
    def customColor(self, r, g, b):
        self.process.terminate()
        self.process = Process(target = self.led.customColor, kwargs={'r':r,'g':g,'b':b})
        self.process.start()
        
    def stop(self):
        self.process.terminate()


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
