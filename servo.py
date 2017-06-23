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


Notes: The Servo is acting up a bit. May need to change to another library.
Need to suppress the warnings that the GPIO library is giving for a cleaner GUI
It warns that the Channel is already in use because it has been serup before.

5 has it in upright position 10 is down

Author: Brian McGinnis and Patrick McGinnis
Date: 6/23/17
"""

import RPi.GPIO as GPIO
import time


def map(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


class Servo:
    pwm = None

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(26, GPIO.OUT)
        self.pwm = GPIO.PWM(26, 50)

    def wave(self, times=5):
        self.armUp()
        while (times > 0):
            self.armDown()
            self.armUp()
            times = times - 1
        self.pwm.stop()

    def angle(self, degrees):
        # degrees MUST BE between 0 and 180
        self.pwm.start(map(degrees, 0, 180, 1, 15))
        time.sleep(.5)
        self.pwm.stop()

    def armUp(self):
        self.angle(30)

    def armDown(self):
        self.angle(120)

# s = servo()
# s.wave(2)
# s.armDown()
# s.armUp()
