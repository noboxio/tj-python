#Author: Brian McGinnis
#Date: June 16 2017
#Rev: 1.1

from watson_developer_cloud import TextToSpeechV1
import json
import wave
import pyaudio
import os.path
from os.path import join, dirname
import subprocess

class TextToSpeech:
        
        def __init__(self, username, password):
                self.user = username
                self.pas = password
                self.text_to_speech = TextToSpeechV1(username=username, password=password, x_watson_learning_opt_out=True)
                self.fileLocation = "resources/output.wav"
  

        def speak(self, message):

                with open(join(dirname(__file__), self.fileLocation), 'wb') as audio_file:
                        audio_file.write(self.text_to_speech.synthesize(message, accept='audio/wav', voice="en-US_AllisonVoice"))
                        
                
                subprocess.call(["aplay", self.fileLocation])
                
                """
                old code going to run it with system calls
                #define stream chunk   
                chunk = 2048
                #open a wav forat music  
                f = wave.open(r"resources/output.wav","rb")  
                #instantiate PyAudio  
                p = pyaudio.PyAudio()  
                #open stream  
                stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(), rate = f.getframerate(), output = True)  
                #read data  
                data = f.readframes(chunk)  
                #play stream  
                while data:  
                        stream.write(data)  
                        data = f.readframes(chunk)  
                        #stop stream
                stream.stop_stream()  
                stream.close()  
                        #close PyAudio  
                p.terminate()
                """

#tts = TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
#tts.speak('I believe I know what you are saying')

