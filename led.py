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
from multiprocessing import Process
import colour
import threading
import re

"""NeoPixel class

This is the NeoPixel class
"""
class NeoPixel:

    def __init__(self):
        """Create an NeoPixel object.

        Creates an NeoPixel object that is based off of the neopixel adafruit stuff
        """
        LED_COUNT = 16
        LED_PIN = 10
        LED_FREQ_HZ = 800000
        LED_DMA = 5
        LED_BRIGHTNESS = 255
        LED_INVERT = False
        LED_CHANNEL = 0
        LED_STRIP = ws.WS2811_STRIP_RGB
        self.strip = Adafruit_NeoPixel(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
            LED_STRIP)
        self.strip.begin()

    def rainbow(self, wait_ms=1, iterations=1):
        """Make the LED go rainbow.

        The led will go between the different colors with a wait and iteration.

        wait_ms -- int miliseconds to wait between changes default=1
        iterations -- number of times to repeat the cycle default=1
        """
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((i + j) & 255))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)

    def rainbow_cycle(self, wait_ms=1, iterations=5):
        """Make the LED go rainbow cycle.

        The led will go between the different colors with a wait and iteration.

        wait_ms -- int miliseconds to wait between changes default=1
        iterations -- number of times to repeat the cycle default=5
        """
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(
                    i,
                    self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)

    def strobe(self):
        """Strobe the led.

        Turn the led on and off rapidly
        """
        wait_ms = 50
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, self.wheel((i + j) % 255))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)

    def wheel(self, pos):
        """Change the color based on the 'wheel'.

        Change the color based on the wheel determined by adafruit

        pos -- int position on the wheel
        """
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def custom_color_rgb(self, r, g, b):
        """Change the color to a custom color.

        Change the color of the LED to the specified color R G B values

        r -- int value of red
        g -- int value of green
        b -- int value of blue
        """
        self.strip.setPixelColorRGB(0, r, g, b)
        self.strip.show()

    def custom_color_name(self, color_name):
        """Change the color of the LED to the specified name color.

        Change the color fo the LED to the specified color value

        color_name -- valid color name or id using colour module
        """
        c = colour.Color(color_name)
        self.custom_color_rgb(int(c.red * 255), int(c.green * 255), int(c.blue * 255))





class LedManager(threading.Thread):
    """LedManager is basically a manager for the led objects.

    it functions as a thread so that the led can be started, stopped or
    whatever whenever
    """
    #not sure if you can set the default like this but we shall see lol
    def __init__(self, led=NeoPixel()):
        """Create an LED Manager type.

        led -- the led that is to be controlled by this process
        """
        threading.Thread.__init__(self)
        self.led = led
        self.process = None
        self.commands = list()

        self.start()

    def run(self):
        """ run as thread"""
        while(True):
            if self.commands:
                cmd = self.commands.pop()
                self.execute_command(cmd)


    def dosleep(self, duration):
        time.sleep(duration)

    def add_command(self, command):
        self.commands.append(command)

    def execute_command(self, command):
        """Execute a command in text form"""


        regex = re.compile(r"^\w+") #selects just the first word
        command_method = regex.match(command).group()
        print("command_method: " + command_method)

        # check to see if the command is in the manager
        if command_method in dir(self):
            #matching command was foudn
            print("matching command found")
            print("self." + command)
            eval("self." + command)
        else:
            print("no matching command found in LedManager")
            if self.led is None:
                print("LED MANAGER: no led is currently active")
            else:
                eval("self.led." + command)


        self.__clearProcess__()
        self.process = Process(target=eval("self.led." + command))
        self.process.start()


    # So the only commands that should be available at the manager level
    # are basically stop, and maybe off?  or is off repetative?

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
