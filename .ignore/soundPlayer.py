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


soundPlayer.py: plays MP3, WAV sound files.

Uses pyaudio to manually write chunks to audio stream.

***DEPRECATED. Using system call instead.***

Author: Brandon Gong
Date: 6/23/17
"""

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
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
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
