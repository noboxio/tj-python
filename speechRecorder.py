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


speechrecorder.py: Records a phrase spoken by the user and writes out
                   to a .WAV file.

speechrecorder.py starts a microphone and listens for a sound with
greater intensity than the threshold.  When there is a sound that
passes the threshold, it begins recording until some time has
passed without another sound greater than the threshold, at which
point we assume that the user has stopped talking and it is safe to
stop recording.

Author: Brandon Gong
Date: 6/23/17
"""

import audioop
from collections import deque
import math
import time
import wave
import pyaudio


class SpeechRecorder:

    # Declare a few constants.

    # Mic stuff.
    CHANNELS = 1
    CHUNK = 16384
    FORMAT = pyaudio.paInt16
    RATE = 48000

    # Previous audio to add on to the beginning
    # in seconds. Added in order to account for possibly cutting off
    # the very beginning of the user's phrase.
    INIT_PADDING = 0.5

    # Sound threshold.  All sounds above this threshold are considered
    # as speech, while below is considered as silence.
    THRESHOLD = 1200

    # The amount of silence allowed after a sound that passes the
    # threshold in seconds.
    SILENCE_LIMIT = 2

    def __init__(
            self,
            channels=1,
            chunk=16384,
            format=pyaudio.paInt16,
            rate=48000,
            init_padding=0.5,
            threshold=1200,
            silence_limit=2,
            autothresh=False):
        self.CHANNELS = channels
        self.CHUNK = chunk
        self.FORMAT = format
        self.RATE = rate
        self.INIT_PADDING = init_padding
        self.THRESHOLD = threshold
        self.SILENCE_LIMIT = silence_limit
        if autothresh:
            self.auto_threshold()

    # automatically calculate threshold.
    # Parameters:
    #   samples: number of chunks to read from microphone.
    #   avgintensities: the top x% of the highest intensites read to be
    #   averaged. By default, the top 20% of the highest intensities will be
    #   averaged together.
    #   padding: how far above the average intensity the voice should be.
    # TODO: check to make sure this is actually beneficial to performance.
    def autoThreshold(self, samples=50, avgintensities=0.2, padding=100):
        if __debug__:
            print("Auto-thresholding...")

        # start a stream.
        #
        # TODO: if we are to wrap these functions in a class, maybe
        # we should just create one pyaudio stream and open it in the
        # constructor.
        p = pyaudio.PyAudio()
        stream = p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK)

        # Get a number of chunks from the stream as determined by the samples
        # arg, and calculate intensity.
        # intensities = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 4)))
        #               for x in range(samples)]
        intensities = [math.sqrt(abs(audioop.avg(stream.read(self.CHUNK), 4)))]

        # sort the list from greatest to least.
        intensities = sorted(intensities, reverse=True)

        # get the first avgintensities percent values from the list.
        self.THRESHOLD = sum(intensities[:int(samples * avgintensities)]) / int(
            samples * avgintensities) + padding

        # clean up
        stream.close()
        p.terminate()

        if __debug__:
            print("Threshold: ", self.THRESHOLD)

    # Gets the phrase from the user.
    # Returns the filename of the .wav file.
    def getPhrase(self, threshold=THRESHOLD, framerate=RATE):

        # name of output file.
        filename = 'file.wav'

        # Start a pyaudio stream.
        p = pyaudio.PyAudio()
        stream = p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            # input_device_index = 1,
            frames_per_buffer=self.CHUNK
        )

        if __debug__:
            print("Mic is up and listening.")

        # list to hold all of the frames of user's speech.
        speech = []

        # this_chunk holds the current chunk of data.
        this_chunk = None

        # deque containing SILENCE_LIMIT seconds of frames when played
        # at RATE.
        silence_buffer = deque(
            maxlen=int(
                self.SILENCE_LIMIT *
                self.RATE /
                self.CHUNK))

        # deque containing INIT_PADDING seconds of frames when played at
        # RATE.
        init_padding = deque(
            maxlen=int(
                self.INIT_PADDING *
                self.RATE /
                self.CHUNK))

        # Have we started recording yet?
        started = False

        while True:
            # read a new chunk of data from the stream.
            this_chunk = stream.read(self.CHUNK)

            # calculate the average intensity for this chunk and append.
            silence_buffer.append(math.sqrt(abs(audioop.avg(this_chunk, 4))))

            # if at least one of the values in silence_buffer is above
            # the threshold, then keep appending to the speech list.
            if sum([x > threshold for x in silence_buffer]) > 0:

                # if we haven't started already, end the listening phase
                if not started:
                    if __debug__:
                        print("Threshold passed. Recording started.")
                    started = True

                # Append this chunk to the speech list.
                speech.append(this_chunk)

            # if already started but nothing above threshold in silence
            # buffer, end recording and write to file.
            elif started is True:

                if __debug__:
                    print("Maximum silence reached.")

                # generate a filename for temporary speech file
                filename = 'resources/speech.wav'

                # concat bytes
                data = ''.join(list(init_padding) + speech)

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
                init_padding.append(this_chunk)

        if __debug__:
            print("Done.  Closing stream.")
        stream.close()
        p.terminate()

        return filename

    # process the phrase, as hinted by the name of the function
    # Possibly call Watson STT here.
    def process_phrase(self, f):
        pass  # process code here


if __name__ == '__main__':
    SpeechRecorder().getPhrase()
