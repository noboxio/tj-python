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
import re


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


class Servo:
    pwm = None

    def __init__(self, up_angle=0, down_angle=180):
        """Constructor for a single servo."""
        self.up_angle = up_angle
        self.down_angle = down_angle
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(26, GPIO.OUT)
        self.pwm = GPIO.PWM(26, 50)
        self.pwm.start(2.5)

    def _log(self, message):
        """Print the log message with the object id.

        message -- string that needs to be logged
        """
        print("|" + str(self) + "| " + str(message) )

    def wave(self, times=5):
        """Wave the arm.
        A wave is defined as going from the down position to the up position once

        times -- the number of times to wave, default = 5
        """
        while (times > 0):
            self.up()
            self.down()
            times = times - 1

    def angle(self, degrees):
        """Set the angle of the servo to a specific angle.

        degrees -- int value of degrees to be set at
                   MUST BE BETWEEN 0 and 180
        map function is used to map the values into useful data for the servos
        we are using.  The out min and max may need to be changed for
        different servos.
        """
        # degrees MUST BE between 0 and 180
        if degrees > 180 or degrees < 0:
            print("INVALID ANGLE SPECIFIED.  MUST BE BETWEEN 0 AND 180")
        else:
            #TODO: Need to figure out how to stop the servo after moving.
            GPIO.setmode(GPIO.BOARD)
            GPIO.cleanup()
            GPIO.setup(26, GPIO.OUT)
            self.pwm = GPIO.PWM(26, 50)
            self.pwm.start(map(degrees, 0, 180, 2.5, 12.5))
            self.pwm.ChangeDutyCycle(map(degrees, 0, 180, 2.5, 12.5))
            time.sleep(1)
            #for i in range(45):
            #    print("SERVO IS DISABLED RIGHT NOW!")
            self.pwm.stop()
            GPIO.cleanup()

    def up(self):
        """Point the arm up, use this to define the up angle
        angle depends on the orientation of the servo

        TODO: perhaps make this a constructor variable?
        """
        self.angle(self.up_angle)

    def down(self):
        """Point the arm down, use this to define the up angle
        angle depends on the orientation of the servo

        TODO: perhaps make this a constructor variable?
        """
        self.angle(self.down_angle)
    def __dir__(self):
        return(['wave', 'angle', 'up', 'down'])



class ServoManager(threading.Thread):
    """ServoManager is basically a manager for the servo objects.

    it functions as a process so that the servo can be started, stopped or
    whatever whenever
    """

    def __init__(self, tj=None, s=Servo()):
        """Create a ServoManager type object.

        s -- Servo to contorl
        TODO: make it control multiple servos?
        """
        threading.Thread.__init__(self)
        self.tj = tj
        self.s = s
        self.commands = list()

    def _log(self, message):
        """Print the log message with the object id.

        message -- string that needs to be logged
        """
        print("|" + str(self) + "| " + str(message) )

    def add_command(self, command):
        """Add a command to the commands list.

        Append the command to the commands list.

        command -- the text command to appent to the commands list.
        """
        self.commands.append(command)


    def run(self):
        """ run as thread"""
        while(True):
            if self.commands:
                cmd = self.commands.pop(0)
                self.execute_command(cmd)

    def set_up(self, up_angle):
        """Set the up value of the servo arm.

        up -- the angle in degrees that is Up
        """
        self.s.up_angle = up_angle

    def set_down(self, down_angle):
        """Set the down value of the servo arm.

        down -- the angle in degrees that is Down
        """
        self.s.down_angle = down_angle

    def execute_command(self, command):
        """Execute a command in text form"""
        regex = re.compile(r"^\w+") #selects just the first word
        command_method = regex.match(command).group()
        self._log("command_method: " + command_method)

        # check to see if the command is in the manager
        if command_method in dir(self):
            #matching command was foudn
            self._log("matching command found")
            self._log("self." + command)
            try:
                eval("self." + command)
            except:
                self._log("there was an exception")
        else:
            self._log("no matching command found in ServoManager")
            if self.s is None:
                self._log("Servo MANAGER: no servo is currently active")
            else:
                try:
                    exec("self.s." + command)
                except:
                    self._log("there was an exception self.s." + command)
    def __dir__(self):
        return([])
