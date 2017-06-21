#!/usr/bin/env python

# TODO: implement mp3

import pyaudio
import wave

class SoundPlayer:

    CHUNK = 1024

    def __init__(self, chunk=1024):
        self.CHUNK = chunk

    # play_WAV: does what the function name says
    def play_WAV(self, filename):

        # open wav file of choice
        wf = wave.open(filename, 'rb')

        # Start a stream
        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
        )

        # Start playing the sound.
        # Read CHUNK amound of frames into a variable, then write that variable
        # to the stream aka play the sound.
        this_chunk = wf.readframes(self.CHUNK)
        while this_chunk:
            stream.write(this_chunk)
            this_chunk = wf.readframes(self.CHUNK)

        # cleanup.
        stream.close()
        p.terminate()


    def play_MP3(self, filename):
        pass


if __name__ == '__main__':
    SoundPlayer().play_WAV("asdfasdf.wav")
