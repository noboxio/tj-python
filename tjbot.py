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


TJBot

Author: Brian McGinnis and Patrick McGinnis
Date: 6/23/17
"""

import led
import servo
import music
import time
import subprocess
from multiprocessing import Process
import sys
import threading
import re
import configparser


class TJBot(threading.Thread):
    """TJBot is a thread that controls the TJ Bot.

    TODO: Need to work on the name.  I am not sure where TJBot is used else where.
    Decided to put it back to TJBot
    """
    import watsonServices

    def __init__(self, name="none"):
        """Create a TJBot type object.

        If a name isn't passed it will default to none.

        name -- the name of the TJBot
        """
        threading.Thread.__init__(self)

        # set TJBot's name
        self.name = name

        # Create a Servo object and also create a ServoManager object
        # to control the servo
        self.servo_manager = servo.ServoManager()
        #self.servo_manager.set_up(180)
        #self.servo_manager.set_down(0)

        # Create a Led object and also create a LedManager object
        # to control the Led
        self.led_manager = led.LedManager()

        # Create a Music object and also create a MusicManager object
        # to control the music
        self.music_manager = music.MusicManager(self)
        # load the music that is in the resources/music folder
        #self.music_manager.load_music()

        # Create the regex object to pull out the data
        self.regex = re.compile(r"~\S+~") #selects just the first word

    def run(self):
        """The run method required by threading.Thread.

        run run's itself when object.start() is called
        """
        # Simple led commands to make the LED go RED --> GREEN --> BLUE to
        # basically show that the TJ Bot is booting
        self.led_manager.add_command("custom_color_name('red')")
        self.led_manager.add_command("wait(1)")
        self.led_manager.add_command("custom_color_name('green')")
        self.led_manager.add_command("wait(1)")
        self.led_manager.add_command("custom_color_name('blue')")
        self.led_manager.add_command("wait(1)")
        self.led_manager.add_command("rainbow(iterations=2)")

        # Make TJ bot wave 3 times
        #self.servo_manager.add_command("wave(3)")

        # Make TJ bot say hello
        self.watsonServices.tts.speak('Hello I am ' + self.name + ' ask me something')

        while(True):
            time.sleep(.001)
            phrase = self.watsonServices.stt.get_phrase()
            if self.name in phrase:
                response = self.watsonServices.convo.sendMessage(phrase)
                response = response.lower()
                response = self.process_response(response)
                self.watsonServices.tts.speak(response)


    def process_response(self, response):
        """Process the response from the converation module or input.

        Cleans the response and sends the detected commands to the proper modules.

        response -- response to process

        Returns a cleaned response of any commands found.

        See the list of available commands that is in the help file.
        THIS WILL NEED TO BE GENERATED EVERY time
        TODO: Write a script or something that creates this list.
        """
        print("response: " + response)

        commands = self.regex.findall(response)
        for cmd in commands:
            print("response: " + response + " | command: " + cmd)
            response = response.replace(cmd,'',1)
            cmd = cmd.replace("~",'',2)

            if 'music.' in cmd:
                print("sending command to music")
                cmd = cmd.replace('music.','',1)
                self.music_manager.execute_command(cmd)

            if 'led.' in cmd:
                print("sending command to led")
                cmd = cmd.replace('led.','',1)
                self.led_manager.add_command(cmd)

            if 'servo.' in cmd:
                cmd = cmd.replace('servo.','',1)
                self.servo_manager.execute_command(cmd)

        return(response)

def console_input(tj):
    """Keep asking for input in the console.

    When input is recieved send it to the process_response method in TJBott.

    tj -- the tjbot to interact with
    """
    while(True):
        try:
            text = input("COMMAND: ")
            tj.process_response(text)
        except:
            print("console_input exception occured")

def main():
    """Main method creates a TJ bot and starts it along with the console_input.

    main method
    """
    settings = configparser.ConfigParser()
    settings.read("settings")

    tj = TJBot(settings.get("tj", "name"))
    tj.start()

    console_input(tj)


if __name__ == "__main__":
    main()
