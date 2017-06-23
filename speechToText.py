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
Date: June 17 2017
Rev: 1.0
"""

import json
import os.path
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


class SpeechToText:

    def __init__(self, username, password):
        self.user = username
        self.pas = password
        self.speech_to_text = SpeechToTextV1(
            username=username,
            password=password,
            x_watson_learning_opt_out=True)

    def transcribe(self):
        if not os.path.exists('resources/speech.wav'):
            return 'I hear nothing'
        with open(join(dirname(__file__), 'resources/speech.wav'), 'rb') as audio_file:
            jsn = json.loads(
                json.dumps(
                    self.speech_to_text.recognize(
                        audio_file,
                        content_type='audio/wav',
                        timestamps=True,
                        word_confidence=True),
                    indent=2))
            # print(jsn['results'][0]['alternatives'][0]['transcript'])
            return jsn['results'][0]['alternatives'][0]['transcript']
