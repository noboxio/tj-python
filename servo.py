#!/usr/bin/env python

"""
Author: Brian McGinnis

Notes: The Servo is acting up a bit. May need to change to another library.
Need to suppress the warnings that the GPIO library is giving for a cleaner GUI
It warns that the Channel is already in use because it has been serup before.

"""


import RPi.GPIO as GPIO
import time

class servo:
        pwm = None

        def __init__(self):
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(26, GPIO.OUT)
                self.pwm=GPIO.PWM(26,50)
                
        def wave(self, times):
                self.pwm.start(5)
                while (self > 0):
                        self.pwm.ChangeDutyCycle(5)
                        time.sleep(.5)
                        self.pwm.ChangeDutyCycle(2)
                self.pwm.stop()

