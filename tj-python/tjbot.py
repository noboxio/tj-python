"""
TJBot
Author: Brian McGinnis
"""

import conversation
import ledProcess
import led
import servoProcess
import servo
import textToSpeech
import streaming
import time

def main():
    stt = streaming.StreamingSTT('1f900d96-d3fa-40f0-ab53-9a600f931796', 'GAyuVqI1EEMv')
    name = 'Alex'
    servo_obj = servo.Servo()
    servoP = servoProcess.ServoProcess(servo_obj)
    led_obj = led.Led()
    ledP = ledProcess.LedProcess(led_obj)
    
    tts = textToSpeech.TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
    convo = conversation.Conversation('1063c5aa-1366-4792-ab2f-e17019a1fed8', 'aM04boXKsMPz', 'e4228507-443b-40be-bc8e-9c30a5d64d08')

    print('armup')
    servoP.armUp()

    time.sleep(.5)
    print('armdown')
    servoP.armDown()
    time.sleep(.5)
    print('armangle')
    servoP.angle(45)
    time.sleep(1)
    print('armwave')
    servoP.wave(5)
    time.sleep(1)

    ledP.strobe()
    print('led waiting')
    time.sleep(3)

    
    """l = led.Led()
    le = ledProcess.LedProcess(l)
    print('sleeping')
    time.sleep(3)
    print('done sleeping, Lets Strobe')
    le.strobe()
    #le.customColor(255,0,0)
    print('sleeping')
    time.sleep(3)
    print('kill in 2')
    time.sleep(2)
    le.customColor(255,0,0)
    #le.stop()
    print('dead') """
    
    tts.speak('Hello I am ' + name + ' ask me something')

    while(1):
        phrase = stt.get_phrase()
        if name in phrase:
            response = convo.sendMessage(phrase)
            response.upper()
            if '~' in response:
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
                if '~WAVE' in response:
                    response = response.replace('~WAVE', '', 1) 
            tts.speak(response)
    

if __name__ == "__main__": main()
                                      
    