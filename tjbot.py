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

#import ledProcess
import led
#import servoProcess
import servo
#import musicProcess
import music
import time
import subprocess
from multiprocessing import Process
import sys

import re


class TJBott:
    import watsonServices

    def __init__(self, name="none"):
        for a in range(100):
            print("making a tjbot")

        # replace with robot name
        self.name = name

        # Create a Servo object and also create a ServoProcess object
        # to control the servo
        #servo_obj = servo.Servo()
        self.servo_manager = servo.ServoManager()

        # Create a Led object and also create a LedProcess object
        # to control the Led
        #self.led_obj = led.NeoPixel()
        self.led_manager = led.LedManager()

        # Create a Music object and also create a MusicProcess object
        # to control the music
        #song = music.Song("/home/pi/tj-python/resources/music.wav")
        #musicP = musicProcess.MusicProcess(music_obj)
        self.music_manager = music.MusicManager()
        self.music_manager.load_music()
        #music_manager.load_song(song)

        # Create the regex object to pull out the data
        self.regex = re.compile(r"~\S+~") #selects just the first word

    def run(self):
        # Simple led commands to make the LED go RED --> GREEN --> BLUE to
        # basically show that the TJ Bot is booting
        time.sleep(.25)
        #ledP.red()
        print("color red")
        time.sleep(.25)
        #ledP.green()
        print("color green")
        time.sleep(.25)
        #ledP.blue()
        print("color blue")
        time.sleep(.25)

        # Make the led do the rainbow cycle for forever!
        #ledP.rainbowCycle(.0001, 99999999999999)

        # Make TJ bot wave 3 times
        self.servo_manager.wave(3)

        # Make TJ bot say hello
        self.watsonServices.tts.speak('Hello I am ' + self.name + ' ask me something')



        while(True):
            time.sleep(.001)
            phrase = self.watsonServices.stt.get_phrase()
            if self.name in phrase:
                response = self.watsonServices.convo.sendMessage(phrase)
                response = response.lower()
                self.process_response(response)



                self.watsonServices.tts.speak(response)


    def process_response(self, response):
        print("response: " + response)


        commands = self.regex.findall(response)
        for cmd in commands:
            print("response: " + response + " | command: " + cmd)
            response = response.replace(cmd,'',1)
            cmd = cmd.replace("~",'',2)
            #TODO execute the command passed.....
            if 'music.' in cmd:
                print("sending command to music")
                cmd = cmd.replace('music.','',1)
                self.music_manager.execute_command(cmd)

            if 'led.' in cmd:
                print("sending command to led")
                cmd = cmd.replace('led.','',1)
                self.led_manager.execute_command(cmd)
            if 'arm.' in cmd:
                self.servo_manager.execute_command(cmd)

                #watsonServices.tts.speak(response)


def console_input(tj):
    while(True):
        text = input("COMMAND: ")
        #tjbot.process_response(text)
        tj.process_response(text)



def main():
    tj = TJBott()

    process_tj = Process(target=tj.run)

    print("fot here")
    process_tj.start()

    console_input(tj)

    #tj.run()





if __name__ == "__main__":
    main()
