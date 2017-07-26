#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
# NOTE: The was taken from the example file inside of the SpeechRecognition git

import speech_recognition as sr




class speechToText:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # obtain audio from the microphone


    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)


        # recognize speech using IBM Speech to Text
        IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
        IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
        try:
            print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
        except sr.UnknownValueError:
            print("IBM Speech to Text could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from IBM Speech to Text service; {0}".format(e))
