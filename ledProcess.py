#!/usr/bin/env python.

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
from multiprocessing import Process
import led


class LedProcess():
    """LedProcess is basically a manager for the led objects.

    it functions as a thread so that the led can be started, stopped or
    whatever whenever
    """

    def __init__(self, led):
        """Create an LED Process type.

        led -- the led that is to be controlled by this process
        """
        self.led = led
        self.process = None

    def strobe(self):
        """Strobe the led.

        Turn the led on and off rapidly or whatever else is programmed
        """
        self.__clearProcess__()
        self.process = Process(target=self.led.strobe)
        self.process.start()

    def rainbow(self, wait_ms, iterations):
        """Make the LED go rainbow.

        The led will go between the different colors with a wait and iteration.

        wait_ms -- int miliseconds to wait between changes
        iterations -- number of times to repeat the cycle
        """
        self.__clearProcess__()
        self.process = Process(
            target=self.led.rainbow,
            kwargs={
                'wait_ms': wait_ms,
                'iterations': iterations})
        self.process.start()

    def rainbowCycle(self, wait_ms, iterations):
        """Make the LED go rainbow cucle.

        The led will go between the different colors with a wait and iteration.

        wait_ms -- int miliseconds to wait between changes
        iterations -- number of times to repeat the cycle
        """
        self.__clearProcess__()
        self.process = Process(
            target=self.led.rainbowCycle,
            kwargs={'wait_ms': wait_ms,
                    'iterations': iterations})
        self.process.start()

    def wheel(self, pos):
        """Change the color based on the 'wheel'.

        Change the color based on the wheel determined by adafruit

        pos -- int position on the wheel
        """
        self.__clearProcess__()
        self.process = Process(target=self.led.wheel, kwargs={'pos': pos})
        self.process.start()

    def customColor(self, r, g, b):
        """Change the color to a custom color.

        Change the color of the LED to the specified color R G B values

        r -- int value of red
        g -- int value of green
        b -- int value of blue
        """
        self.__clearProcess__()
        self.process = Process(
            target=self.led.customColor,
            kwargs={'r': r,
                    'g': g,
                    'b': b})
        self.process.start()

    def red(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(255, 0, 0)

    def orange(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(255, 127, 0)

    def yellow(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(255, 255, 0)

    def green(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(0, 255, 0)

    def blue(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(0, 0, 255)

    def purple(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(127, 0, 255)

    def pink(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(255, 0, 255)

    def white(self):
        """Set color.

        Set the color to the color specified
        """
        self.customColor(255, 255, 255)

    def off(self):
        """Set color.

        Set the color to the color specified
        """
        self.stop()

    def stop(self):
        """Stop all leds.

        calls the __clearProcess__ function to stop all processes
        """
        self.__clearProcess__()

    def __clearProcess__(self):
        """Stop all existing process under this process.

        stops all led processes running.
        """
        if self.process is not None:
            self.process.terminate()

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
