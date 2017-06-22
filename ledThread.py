"""
Author: Brian McGinnis and Patrick McGinnis
"""

import time
from neopixel import *
import threading


class LedThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        
        LED_COUNT = 16
        LED_PIN = 10
        LED_FREQ_HZ = 800000
        LED_DMA = 5
        LED_BRIGHTNESS = 255
        LED_INVERT = False
        LED_CHANNEL = 0
        LED_STRIP = ws.WS2811_STRIP_RGB
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()
        
    def run(self):
        while True:
            #print("ledThread running - " + self.name)
            time.sleep(.5)
            
    def strobe(self):
        wait_ms = 50

        for j in range(256):
            for i in range(0, self.strip.numPixels(), 3):
                self.strip.setPixelCOlor(i+q, self.wheel((i+j) % 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, self.strip.numPixels(), 3):
                self.strip.setPixelColor(i+q, 0)
                
    def wheel(self,pos):
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
        
    def customColor(self, r, g, b):
        self.strip.setPixelColorRGB(0, r, g, b)
        self.strip.show()



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
