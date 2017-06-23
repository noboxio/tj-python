"""
TJBot
Author: Brian McGinnis
"""

import conversation
import ledThread
import led
import servoThread
import textToSpeech
import streaming
import time

def main():
    stt = streaming.StreamingSTT('1f900d96-d3fa-40f0-ab53-9a600f931796', 'GAyuVqI1EEMv')
    
    #servo = servoThread.ServoThread()
    tts = textToSpeech.TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
    convo = conversation.Conversation('1063c5aa-1366-4792-ab2f-e17019a1fed8', 'aM04boXKsMPz', 'e4228507-443b-40be-bc8e-9c30a5d64d08')
    """servo.daemon = True
    servo.start()"""
    l = led.Led()
    le = ledThread.LedThread(l)
    name = 'Alex'
    print('sleeping')
    time.sleep(3)
    print('done sleeping, Lets Strobe')
    le.strobe()
    print('sleeping')
    time.sleep(3)
    print('done')

    tts.speak('Hello I am ' + name + ' ask me something')

    while(1):
        tts.speak(convo.sendMessage(stt.get_phrase()))
        print('phrase')
        time.sleep(5)
    

if __name__ == "__main__": main()
                                      
    
