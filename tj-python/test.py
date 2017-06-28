"""
Author: Brian McGinnis

"""

import conversation
import led
import servo
import textToSpeech
import speechToText
import speechrecorder

#print('ILY')
def main():
    
    con = conversation.conversation('154b5b29-d1ca-4ff2-be09-c33c5e1d9e20' , 'pmNftYlpvMS8','9ef80568-2a3b-4790-a8e0-363c0bc7d237')
    tts = textToSpeech.TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
    stt = speechToText.SpeechToText('1f900d96-d3fa-40f0-ab53-9a600f931796', 'GAyuVqI1EEMv')
    sr = speechrecorder.SpeechRecorder()
    sr.get_phrase()
    print(stt.s2t())
    tts.speak(stt.s2t())
    print('ILY')
    tts.speak("Hello, I am alive")
    l = led.led()
    s = servo.servo()
    l.customColor(255,0,0)
    s.wave(2)
    
    

if __name__ == "__main__": main()
#    print('ILY')
