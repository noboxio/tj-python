#!/usr/bin/env python

"""
Author: Brian McGinnis and Patrick McGinnis

Notes: The Servo is acting up a bit. May need to change to another library.
Need to suppress the warnings that the GPIO library is giving for a cleaner GUI
It warns that the Channel is already in use because it has been serup before.

5 has it in upright position 10 is down

"""


import RPi.GPIO as GPIO
import time
import threading

class ServoThread(threading.Thread):
        pwm = None

        def __init__(self):
                threading.Thread.__init__(self)
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(26, GPIO.OUT)
                self.pwm=GPIO.PWM(26,50)
                
                
        def run(self):
                while True:
                        #print("ledThread running - " + self.name)
                        time.sleep(.5)
                
        def wave(self, times):
                self.pwm.start(5)
                while (times > 0):
                        self.pwm.ChangeDutyCycle(10)
                        time.sleep(1)
                        self.pwm.ChangeDutyCycle(5)
                        time.sleep(1)
                        times = times - 1
                self.pwm.stop()

        def armUp(self):
                self.pwm.start(5)
                time.sleep(2)
                self.pwm.stop()
                
        def armDown(self):
                self.pwm.start(10)
                time.sleep(2)
                self.pwm.stop()
#s = servo()
#s.wave(2)
#s.armDown()
#s.armUp()
