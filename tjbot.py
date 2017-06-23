"""
TJBot
Author: Brian McGinnis
"""

import conversation
import ledThread
import servoThread
import textToSpeech
import streaming
import time

def main():
    stt = streaming.StreamingSTT('1f900d96-d3fa-40f0-ab53-9a600f931796', 'GAyuVqI1EEMv')
    led = ledThread.LedThread()
    servo = servoThread.ServoThread()
    tts = textToSpeech.TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
    convo = conversation.Conversation('154b5b29-d1ca-4ff2-be09-c33c5e1d9e20', 'pmNftYlpvMS8', '65cc98a8-a10b-4d03-ac7d-419f02d1e23b')
    servo.daemon = True
    servo.start()
    led.daemon = True
    led.start()
    print('sleeping')
    time.sleep(3)
    print('done sleeping, Lets Strobe')
    #led.strobe()
    print('sleeping')
    time.sleep(3)
    print('done')

if __name__ == "__main__": main()
                                      
    
