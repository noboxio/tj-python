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


Author: Brian McGinnis
Date: June 16 2017
Rev: 1.1
"""

from watson_developer_cloud import TextToSpeechV1
import json
import wave
import pyaudio
import os.path
from os.path import join, dirname
import subprocess


class TextToSpeech:
    """TextToSpeech class uses watson tts service."""

    def __init__(self, username, password):
        """Cereate TextToSpeech object to work with watson services.

        username -- username for watson tts service
        password -- password for watson tts service
        """
        self.user = username
        self.pas = password
        self.text_to_speech = TextToSpeechV1(
            username=username,
            password=password,
            x_watson_learning_opt_out=True)
        self.fileLocation = "/home/pi/tj-python/resources/output.wav"

    def speak(self, message):
        """Speak a text message.

        message - the text string to be played.
        """
        with open(join(dirname(__file__), self.fileLocation), 'wb') as audio_file:
                audio_file.write(
                    self.text_to_speech.synthesize(
                        message,
                        accept='audio/wav',
                        voice="en-US_AllisonVoice"))

        subprocess.call("exec aplay " + self.fileLocation, shell=True)

        # old code going to run it with system calls
        # define stream chunk
        # chunk = 4096
        # open a wav forat music
        # f = wave.open(r"resources/output.wav","rb")
        # instantiate PyAudio
        # p = pyaudio.PyAudio()
        # open stream
        # stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
        # channels = f.getnchannels(), rate = f.getframerate(), output = True)
        # read data
        # data = f.readframes(chunk)
        # play stream
        # while data:
        #         stream.write(data)
        #         data = f.readframes(chunk)
        # stop stream
        # stream.stop_stream()
        # stream.close()
        # close PyAudio
        # p.terminate()

# tts = TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
# tts.speak('I believe I know what you are saying')
