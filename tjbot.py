"""
TJBot
Author: Brian McGinnis
"""

import conversation
import ledProcess
import led
import servoThread
import textToSpeech
import streaming
import time

def main():
    stt = streaming.StreamingSTT('1f900d96-d3fa-40f0-ab53-9a600f931796', 'GAyuVqI1EEMv')
    name = 'Alex'
    #servo = servoThread.ServoThread()
    tts = textToSpeech.TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
    convo = conversation.Conversation('1063c5aa-1366-4792-ab2f-e17019a1fed8', 'aM04boXKsMPz', 'e4228507-443b-40be-bc8e-9c30a5d64d08')
    #servo.daemon = True
    #servo.start()
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
            respone.upper()
            if '~' in response:
                if '~RED' in response:
                    le.red()
                    response.replace('~RED', '', 1)
                if '~ORANGE' in response:
                    le.orange()
                    response.replace('~ORANGE', '', 1)
                if '~YELLOW' in response:
                    le.yellow()
                    response.replace('~YELLOW', '', 1)
                if '~GREEN' in response:
                    le.green()
                    response.replace('~GREEN', '', 1)
                if '~BLUE' in response:
                    le.blue()
                    response.replace('~BLUE', '', 1)
                if '~PURPLE' in response:
                    le.purple()
                    response.replace('~PURPLE', '', 1)
                if '~PINK' in response:
                    le.pink()
                    response.replace('~PINK', '', 1)
                if '~WHITE' in response:
                    le.white()
                    response.replace('~WHITE', '', 1)
                """if '~WAVE' in response:
                    response.replace('~WAVE', '', 1) """
            tts.speak(response)
    

if __name__ == "__main__": main()
                                      
    
