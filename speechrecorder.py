#!/usr/bin/env python

import pyaudio
import wave
import audioop
from collections import deque
import time
import math

"""
speechrecorder.py: Records a phrase spoken by the user and writes out
                   to a .WAV file.

speechrecorder.py starts a microphone and listens for a sound with
greater intensity than the threshold.  When there is a sound that
passes the threshold, it begins recording until some time has
passed without another sound greater than the threshold, at which
point we assume that the user has stopped talking and it is safe to
stop recording.

TODO: Add a method to automatically set threshold.  Different
      microphones might pick up different sound intensities, and some
      environments might just have a louder average sound intensity
      than others.  With a preset threshold, this code might only work
      well on certain microphones.

Author: Brandon Gong
"""

# Declare a few constants.

# Mic stuff.
CHANNELS = 1
CHUNK    = 1024
FORMAT   = pyaudio.paInt16
RATE     = 16000

# Sound threshold.  All sounds above this threshold are considered
# as speech, while below is considered as silence.
THRESHOLD = 2500

# The amount of silence allowed after a sound that passes the
# threshold in seconds.
SILENCE_LIMIT = 2

# Previous audio to add on to the beginning
# in seconds. Added in order to account for possibly cutting off
# the very beginning of the user's phrase.
PREV_AUDIO = 0.5

# Gets the phrase from the user.
# Returns the filename of the .wav file.
def getPhrase(threshold=THRESHOLD, framerate=RATE):

    # name of output file.
    filename = ''

    # Start a pyaudio stream.
    p = pyaudio.PyAudio()
    stream = p.open (
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    if __debug__:
        print "Mic is up and listening."

    # list to hold all of the frames of user's speech.
    speech = []

    # this_chunk holds the current chunk of data.
    this_chunk = None

    # deque containing SILENCE_LIMIT seconds of frames when played
    # at RATE.
    silence_buffer = deque( maxlen = SILENCE_LIMIT * RATE / CHUNK )

    # deque containing PREV_AUDIO seconds of frames when played at
    # RATE.
    prev_audio = deque( maxlen = PREV_AUDIO * RATE / CHUNK )

    # Have we started recording yet?
    started = False

    while True:
        # read a new chunk of data from the stream.
        this_chunk = stream.read(CHUNK)

        # calculate the average intensity for this chunk and append.
        silence_buffer.append(math.sqrt(abs(audioop.avg(this_chunk, 4))))

        # if at least one of the values in silence_buffer is above
        # the threshold, then keep appending to the speech list.
        if(sum([x > THRESHOLD for x in silence_buffer]) > 0):

            # if we haven't started already, end the listening phase
            if not started:
                if __debug__:
                    print "Threshold passed. Recording started."
                started = True

            # Append this chunk to the speech list.
            speech.append(this_chunk)

        # if already started but nothing above threshold in silence
        # buffer, end recording and write to file.
        elif (started is True):

            if __debug__:
                print "Maximum silence reached."

            # generate a filename for temporary speech file
            filename = 'temp_' + str(int(time.time())) + '.wav'

            # concat bytes
            data = ''.join(list(prev_audio) + speech)

            # Write!
            wf = wave.open(filename, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(framerate)
            wf.writeframes(data)
            wf.close()
            break

        else:
            # Haven't started yet, but also nothing above threshold;
            # keep listening.
            prev_audio.append(this_chunk)

    if __debug__:
        print "Done.  Closing stream."
    stream.close()
    p.terminate()

    return filename

def processPhrase(f):
    pass # process code here

if(__name__ == '__main__'):
    # processPhrase(getPhrase())
    getPhrase()
