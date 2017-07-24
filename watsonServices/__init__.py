import configparser
import io
from .textToSpeech import *
from .conversation import *
from .speechToText import *

from .streaming import *
import time



# read in the config file
#auth = configparser.RawConfigParser(allow_no_value=True)
settings = configparser.ConfigParser()
settings.read("settings")

stt = streaming.StreamingSTT(
    # replace with speech to text credentials username
    settings.get("stt", "username"),
    # replace with speech to text credentials password
    settings.get("stt", "password"))

tts = textToSpeech.TextToSpeech(
    # replace with text to speech credentials username
    settings.get("tts", "username"),
    # replace with text to speech credentials password
    settings.get("tts", "password"))

convo = conversation.Conversation(
    # replace with conversation credentials username
    settings.get("conversation", "username"),
    # replace with conversation credentials password
    settings.get("conversation", "password"),
    # replace with workspace ID.
    settings.get("conversation","workspaceid"))
