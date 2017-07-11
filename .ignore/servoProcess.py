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
It warns that the Channel is already in use because it has been setup before.

Author: Brian McGinnis and Patrick McGinnis
Date: 6/23/17
"""

import time
from multiprocessing import Process
import servo


class ServoProcess:
    """ServoProcess is basically a manager for the servo objects.

    it functions as a process so that the servo can be started, stopped or
    whatever whenever
    """

    def __init__(self, servo):
        """Create a ServoProcess type object.

        servo -- Servo to contorl
        TODO: make it control multiple servos?
        """
        self.servo = servo
        self.process = None

    def wave(self, times):
        """Wave the arm.

        Wave the arm a certian number of times

        times -- int count of time to wave
        """
        self.__clearProcess__()
        self.process = Process(target=self.servo.wave, kwargs={'times': times})
        self.process.start()

    def angle(self, degrees):
        """Set the servo to a specific angle.

        degrees -- int amount of degrees to be set at
        """
        self.__clearProcess__()
        self.process = Process(
            target=self.servo.angle,
            kwargs={'degrees': degrees})
        self.process.start()

    def armUp(self):
        """Set servo in the "UP" position."""
        self.__clearProcess__()
        self.process = Process(target=self.servo.armUp)
        self.process.start()

    def armDown(self):
        """Set servo in the "DOWN" position."""
        self.__clearProcess__()
        self.process = Process(target=self.servo.armDown)
        self.process.start()

    def stop(self):
        """Call the clear process method that stops all servos in this manager."""
        self.__clearProcess__()

    def __clearProcess__(self):
        """Stop all processes running with regards to the servos."""
        if self.process is not None:
            self.process.terminate()

# s = servo()
# s.wave(2)
# s.armDown()
# s.armUp()
