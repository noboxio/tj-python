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
import threading
import re


class TJBott(threading.Thread):
    import watsonServices

    def __init__(self, name="none"):
        threading.Thread.__init__(self)

        # set TJBot's name
        self.name = name

        # Create a Servo object and also create a ServoManager object
        # to control the servo
        # self.servo_manager = servo.ServoManager()

        # Create a Led object and also create a LedManager object
        # to control the Led
        self.led_manager = led.LedManager()

        # Create a Music object and also create a MusicManager object
        # to control the music
        self.music_manager = music.MusicManager()
        # load the music that is in the resources/music folder
        self.music_manager.load_music()

        # Create the regex object to pull out the data
        self.regex = re.compile(r"~\S+~") #selects just the first word

    def run(self):
        # Simple led commands to make the LED go RED --> GREEN --> BLUE to
        # basically show that the TJ Bot is booting
        self.led_manager.add_command("led.custom_color_name('red')")
        self.led_manager.add_command("wait(1)")
        self.led_manager.add_command("led.custom_color_name('green')")
        self.led_manager.add_command("wait(1)")
        self.led_manager.add_command("led.custom_color_name('blue')")
        self.led_manager.add_command("wait(1)")
        self.led_manager.add_command("led.rainbow())")


        # Make the led do the rainbow cycle for forever!
        #ledP.rainbowCycle(.0001, 99999999999999)

        # Make TJ bot wave 3 times
        #self.servo_manager.wave(3)

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
                self.led_manager.add_command(cmd)
            if 'arm.' in cmd:
                self.servo_manager.execute_command(cmd)

                #watsonServices.tts.speak(response)


def console_input(tj):
    while(True):
        try:
            text = input("COMMAND: ")
            #tjbot.process_response(text)
            tj.process_response(text)
        except:
            print("console_input exception occured")



def main():
    tj = TJBott()

    #process_tj = Process(target=tj.run)

    print("fot here")
    #process_tj.start()
    tj.start()

    console_input(tj)

    #tj.run()





if __name__ == "__main__":
    main()
