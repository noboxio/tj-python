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


def main():

    # replace with robot name
    name = 'ENTER_ROBOT_NAME'

    # Create a Servo object and also create a ServoProcess object
    # to control the servo
    servo_obj = servo.Servo()
    #servoP = servoProcess.ServoProcess(servo_obj)

    # Create a Led object and also create a LedProcess object
    # to control the Led
    led_obj = led.Led()
    #ledP = ledProcess.LedProcess(led_obj)

    # Create a Music object and also create a MusicProcess object
    # to control the music
    music_obj = music.Music("/home/pi/tj-python/resources/music.wav")
    #musicP = musicProcess.MusicProcess(music_obj)

    # Simple led commands to make the LED go RED --> GREEN --> BLUE to
    # basically show that the TJ Bot is booting
    time.sleep(1)
    ledP.red()
    time.sleep(1)
    ledP.green()
    time.sleep(1)
    ledP.blue()
    time.sleep(1)

    # Make the led do the rainbow cycle for forever!
    #ledP.rainbowCycle(.0001, 99999999999999)

    # Make TJ bot wave 3 times
    servoP.wave(3)

    # Make TJ bot say hello
    watsonServices.tts.speak('Hello I am ' + name + ' ask me something')


    while(1):
        phrase = watsonServices.stt.get_phrase()
        if name in phrase:
            response = watsonServices.convo.sendMessage(phrase)
            response = response.upper()
            while '~' in response:
                print("response: " + response)
                watsonServices.tts.speak(response)

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


if __name__ == "__main__":
    main()
