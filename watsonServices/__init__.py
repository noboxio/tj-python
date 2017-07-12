import configparser
import io
from textToSpeech import tts
from conversation import convo

from streaming import *
import time



# read in the config file
auth = configparser.RawConfigParser(allow_no_value=True)
auth.read("auth")

stt = streaming.StreamingSTT(
    # replace with speech to text credentials username
    auth.get("stt", "username"),
    # replace with speech to text credentials password
    auth.get("stt", "password"))

tts = textToSpeech.TextToSpeech(
    # replace with text to speech credentials username
    auth.get("tts", "username"),
    # replace with text to speech credentials password
    auth.get("tts", "password"))

convo = conversation.Conversation(
    # replace with conversation credentials username
    auth.get("convo", "username"),
    # replace with conversation credentials password
    auth.get("convo", "password"),
    # replace with workspace ID.
    auth.get("convo","workspaceid"))
