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
import watsonServices
import re


class TJBot:
    def __init___(self, name):

        # replace with robot name
        self.name = name

        # Create a Servo object and also create a ServoProcess object
        # to control the servo
        #servo_obj = servo.Servo()
        self.servo_manager = servo.ServoManager()

        # Create a Led object and also create a LedProcess object
        # to control the Led
        self.led_obj = led.NeoPixel()
        #ledP = ledProcess.LedProcess(led_obj)

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
        print("color")
        time.sleep(.25)
        #ledP.green()
        print("color")
        time.sleep(.25)
        #ledP.blue()
        print("color")
        time.sleep(.25)

        # Make the led do the rainbow cycle for forever!
        #ledP.rainbowCycle(.0001, 99999999999999)

        # Make TJ bot wave 3 times
        self.servo_manager.wave(3)

        # Make TJ bot say hello
        self.watsonServices.tts.speak('Hello I am ' + self.name + ' ask me something')



        while(1):
            time.sleep(.001)
            phrase = self.watsonServices.stt.get_phrase()
            if name in phrase:
                response = self.watsonServices.convo.sendMessage(phrase)
                response = response.lower()
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
                    if 'led' in cmd:
                        pass
                        #TODO implement this
                    if 'arm' in cmd:
                        self.servo_manager.execute_command(cmd)



                self.watsonServices.tts.speak(response)


    def process_commands(string):

        """
        # This processes the conversation commands from the conversation service
        while(1):
            phrase = watsonServices.stt.get_phrase()
            if name in phrase:
                response = watsonServices.convo.sendMessage(phrase)
                response = response.upper()
                if '~' in response:
                    print('Command Found')
                    if '~RED' in response:
                        ledP.red()
                        response = response.replace('~RED', '', 1)
                    if '~ORANGE' in response:
                        ledP.orange()
                        response = response.replace('~ORANGE', '', 1)
                    if '~YELLOW' in response:
                        ledP.yellow()
                        response = response.replace('~YELLOW', '', 1)
                    if '~GREEN' in response:
                        ledP.green()
                        response = response.replace('~GREEN', '', 1)
                    if '~BLUE' in response:
                        print('Its Blue')
                        ledP.blue()
                        response = response.replace('~BLUE', '', 1)
                    if '~PURPLE' in response:
                        ledP.purple()
                        response = response.replace('~PURPLE', '', 1)
                    if '~PINK' in response:
                        ledP.pink()
                        response = response.replace('~PINK', '', 1)
                    if '~WHITE' in response:
                        ledP.white()
                        response = response.replace('~WHITE', '', 1)
                    if '~RAINBOW' in response:
                        ledP.rainbow()
                        response = response.replace('~RAINBOW', '', 1)
                    if '~RAINBOWCYCLE' in response:
                        ledP.rainbowCycle()
                        response = response.replace('~RAINBOWCYCLE', '', 1)
                    if '~MUSICPLAY' in response:
                        musicP.play()
                        response = response.replace('~MUSICPLAY', '', 1)
                    if '~MUSICSTOP' in response:
                        musicP.stop()
                        response = response.replace('~MUSICSTOP', '', 1)
                    if '~LEDOFF' in response:
                        ledP.off()
                        response = response.replace('~LEDOFF', '', 1)
                    if '~ARMSTOP' in response:
                        servoP.stop()
                        response = response.replace('~ARMSTOP', '', 1)
                    if '~ARMUP' in response:
                        servoP.armUp()
                        response = response.replace('~ARMUP', '', 1)
                    if '~ARMDOWN' in response:
                        servoP.armDown()
                        response = response.replace('~ARMDOWN', '', 1)
                    if '~DANCE' in response:
                        servoP.wave(10)
                        ledP.rainbowCycle(1, 50)
                        response = response.replace('~DANCE', '', 1)
                    if '~ARMANGLE' in response:
                        response = response.replace('~ARMANGLE', '', 1)
                        param = int(response.split("~", 1)[0])
                        response = response.split("~", 1)[1]
                        servoP.angle(param)
                    if '~ARMWAVECOUNT' in response:
                        response = response.replace('~ARMWAVECOUNTARMANGLE', '', 1)
                        param = int(response.split("~", 1)[0])
                        response = response.split("~", 1)[1]
                        servoP.wave(param)
                    if '~ARMWAVE' in response:
                        servoP.wave(2)
                        response = response.replace('~ARMWAVE', '', 1)
                    if response == '':
                        response = 'akward silence'
                """
                #watsonServices.tts.speak(response)


    def console_input():
        print('nothi9n')

def main():
    tj = TJBot("noname")
    tj.run()



if __name__ == "__main__":
    main()
