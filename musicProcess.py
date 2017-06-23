"""
Author: Brian McGinnis and Patrick McGinnis
"""

import time
from neopixel import *
from multiprocessing import Process
import led




class MusicProcess():

    def __init__(self, led):
        self.led = led
        self.process = None
        
            
    def strobe(self):
        self.__clearProcess__()
        self.process = Process(target = self.led.strobe)
        self.process.start()
                
    def wheel(self,pos):
        self.__clearProcess__()
        self.process = Process(target = self.led.wheel, kwargs={'pos':pos})
        self.process.start()
        
    def customColor(self, r, g, b):
        self.__clearProcess__()
        self.process = Process(target = self.led.customColor, kwargs={'r':r,'g':g,'b':b})
        self.process.start()
        

            
    def red(self):
        self.customColor(255, 0, 0)
        
    def orange(self):
        self.customColor(255, 127, 0)

    def yellow(self):
        self.customColor(255, 255, 0)
    
    def green(self):
        self.customColor(0, 255, 0)
        
    def blue(self):
        self.customColor(0, 255, 0)
    
    def purple(self):
        self.customColor(127, 0, 255)
        
    def pink(self):
        self.customColor(255, 0, 255)
    
    def white(self):
        self.customColor(255, 255, 255)
        
    def off(self):
        self.stop()
            
    def stop(self):
        self.__clearProcess__()
        
    def __clearProcess__(self):
        if self.process != None:
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
