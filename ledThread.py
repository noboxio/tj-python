#!/usr/bin/env python

"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio

Author: Brian McGinnis and Patrick McGinnis
Date: 6/23/17
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
        self.thread = threading.Thread(target=self.led.strobe)
        self.thread.start()

    def wheel(self, pos):
        self.__clearThread__()
        self.thred = threading.Thread(
            target=self.led.wheel,
            kwargs={'pos': pos})
        self.thread.start()

    def customColor(self, r, g, b):
        self.__clearThread__()
        self.thread = threading.Thread(
            target=self.led.customColor,
            kwargs={'r': r,
                    'g': g,
                    'b': b})
        self.thread.start()

    def __clearThread__(self):
        if self.thread is not None:
            self.thread.cancel()

    def stop(self):
        self.__clearThread__()


# l = LedThread("ID", "NAME")
# l.daemon = True
# l.start()
#
# print("sleeping")
# time.sleep(5)
# print("dome sleepoing")
# l.changename("hey hey")
# print("name changed")
#
#
# print("sleeping again")
# time.sleep(5)
