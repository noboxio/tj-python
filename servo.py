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

Author: Brian McGinnis and Patrick McGinnis
Date: 6/23/17
"""

import RPi.GPIO as GPIO
import time
from multiprocessing import Process
import threading


def map(x, in_min, in_max, out_min, out_max):
    """Method taken from arduino library that maps a min and max to another
    min and max linearly.

    example: in_min = 0 in_max = 10 out_min = 0 out_max = 20
        if you input 0 --> 0
                     1 --> 2
                     5 --> 10
    it works in both directions, min must always be less than max

    Returns an int or double, not really sure
    """
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


class Servo(threading.Thread):
    pwm = None

    def __init__(self, up=0, down=0):
        """Constructor for a single servo."""
        self.up = up
        self.down = down
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(26, GPIO.OUT)
        self.pwm = GPIO.PWM(26, 50)

    def wave(self, times=5):
        """Wave the arm.
        A wave is defined as going from the down position to the up position once

        times -- the number of times to wave, default = 5
        """
        while (times > 0):
            self.armUp()
            self.armDown()
            times = times - 1
        self.pwm.stop()

    def angle(self, degrees):
        """Set the angle of the servo to a specific angle.

        degrees -- int value of degrees to be set at
                   MUST BE BETWEEN 0 and 180
        map function is used to map the values into useful data for the servos
        we are using.  The out min and max may need to be changed for
        different servos.
        """
        # degrees MUST BE between 0 and 180
        if angle > 180 or angle < 0:
            print("INVALID ANGLE SPECIFIED.  MUST BE BETWEEN 0 AND 180")
        else:
            self.pwm.start(map(degrees, 0, 180, 1, 15))
            time.sleep(.5)
            self.pwm.stop()

    def armUp(self):
        """Point the arm up, use this to define the up angle
        angle depends on the orientation of the servo

        TODO: perhaps make this a constructor variable?
        """
        self.angle(self.up)

    def armDown(self):
        """Point the arm down, use this to define the up angle
        angle depends on the orientation of the servo

        TODO: perhaps make this a constructor variable?
        """
        self.angle(self.down)




class ServoManager:
    """ServoManager is basically a manager for the servo objects.

    it functions as a process so that the servo can be started, stopped or
    whatever whenever
    """

    def __init__(self, servo=Servo()):
        """Create a ServoManager type object.

        servo -- Servo to contorl
        TODO: make it control multiple servos?
        """
        self.servo = servo
        self.process = None

    def __clearProcess__(self):
        """Stop all processes running with regards to the servos."""
        if self.process is not None:
            self.process.terminate()
