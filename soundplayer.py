#!/usr/bin/env python

import pyaudio
import wave

CHUNK = 1024


def play_WAV(filename):

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
    this_chunk = wf.readframes(CHUNK)
    while this_chunk:
        stream.write(this_chunk)
        this_chunk = wf.readframes(CHUNK)

    # cleanup stuff.
    stream.close()
    p.terminate()


def play_MP3(filename):
    pass


if __name__ == '__main__':
    play_WAV("asdfasdf.wav")
