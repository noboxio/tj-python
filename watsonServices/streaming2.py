#!/usr/bin/env python3

"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio


streaming2.py: rewrite of streaming.py

Author: Brandon Gong
Date: 7/28/17
"""

import sys
import ssl
import base64
import json
import threading
import time
import pyaudio
import websocket
import logging
import math
import audioop
from websocket._abnf import ABNF


class StreamingSTT:

    # Mic config.
    CHUNK = 16384
    FORMAT = pyaudio.paInt16
    # It is necessary to keep CHANNELS at 1. Streaming STT does not handle the
    # extra data well and returns unwanted hums.
    CHANNELS = 1
    RATE = 48000

    # large array of json data returned by watson.
    FINAL = []

    # Threshold: above this point it is considered user speech, below this
    # point it is considered silence.
    THRESHOLD = 1500

    # The amount of silence allowed after a sound that passes the
    # threshold in seconds.
    SILENCE_LIMIT = 2

    # timeout
    TIMEOUT = 10

    # the actual websocket
    WS = None

    # Unblock the read_audio thread once watson final return is recieved
    FINAL_RECEIVED = None

    # Sleep timer.
    SLEEP_TIMER = None
    # Current level of sleepiness
    IS_SLEEPING = False
    # how many minutes to sleep after.
    SLEEP_AFTER = 2

    # the robot name
    ROBOT_NAME = None

    # Constructor.  Basically all you really need is StreamingSTT(<username>,
    # <password>)
    def __init__(
            self,
            username,
            password,
            robot_name,
            logfile=False,
            loglevel=logging.DEBUG,
            auto_threshold=False
    ):
        self.userpass = ":".join((username, password))
        if logfile:
            logging.basicConfig(filename='streaming.log', level=loglevel)
        else:
            logging.basicConfig(level=loglevel)
        self.p = pyaudio.PyAudio()
        if auto_threshold:
            auto_threshold()
        self.FINAL_RECEIVED = threading.Event()
        self.ROBOT_NAME = robot_name

    # Set the timeout
    def set_timeout(self, timeout):
        self.TIMEOUT = timeout

    # Get the timeout
    def get_timeout(self):
        return self.TIMEOUT

    # Set the chunk size
    def set_chunk(self, chunk):
        self.CHUNK = chunk

    # Get the chunk size
    def get_chunk(self, chunk):
        return self.CHUNK

    # Set pyaudio format
    def set_format(self, paformat):
        self.FORMAT = paformat

    # Get pyaudio format
    def get_format(self):
        return self.FORMAT

    # Set frame rate
    def set_rate(self, rate):
        self.RATE = rate

    # Get frame rate
    def get_rate(self):
        return self.RATE

    # Set silence threshold
    def set_threshold(self, threshold):
        self.THRESHOLD = threshold

    # Get silence threshold
    def get_threshold(self):
        return self.THRESHOLD

    # Set silence limit (in seconds)
    def set_silence_limit(self, silence_limit):
        self.SILENCE_LIMIT = silence_limit

    # Get the silence limit (in seconds)
    def get_silence_limit(self):
        return SILENCE_LIMIT

    # Set sleep-after minutes
    def set_sleep_after(self, sleep_after):
        self.SLEEP_AFTER = sleep_after

    # get sleep-after minutes
    def get_sleep_after(self):
        return self.SLEEP_AFTER

    # automatically calculate threshold.
    # Parameters:
    #   samples: number of chunks to read from microphone.
    #   avgintensities: the top x% of the highest intensites read to be
    #   averaged. By default, the top 20% of the highest intensities will be
    #   averaged together.
    #   padding: how far above the average intensity the voice should be.
    # TODO: tweak
    def auto_threshold(self, samples=50, avgintensities=0.2, padding=10):
        logging.info("Auto-thresholding...")

        # start a stream
        stream = self.p.open(format=self.FORMAT,
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

        logging.info("Threshold: {}".format(self.THRESHOLD))

    # read_audio starts a stream and sends chunks to watson real-time.
    def read_audio(self, ws, timeout):

        # get a stream
        #p = pyaudio.PyAudio()

        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK)

        logging.info("Starting recording")

        # silence_chunks is a counter variable counting number of chunks with
        # silence. Once this value surpasses the silence limit, stop recording.
        silence_chunks = 0
        limit_chunks = self.SILENCE_LIMIT * self.RATE / self.CHUNK

        while True:

            logging.debug(str(silence_chunks) + " | " + str(limit_chunks))
            if silence_chunks >= limit_chunks:
                # Get the final response from watson (waiting for 1 second to get it
                # back)
                data = {"action": "stop"}
                logging.info("Phrase terminated, waiting for response")

                # BUG(S): LOTS OF ERRORS ON THIS LINE AAAAAAAAAAHHHHHHHHHHHHHHHH
                ws.send(json.dumps(data).encode('utf8'))
                self.FINAL_RECEIVED.wait(self.TIMEOUT)
                silence_chunks = 0
                self.FINAL_RECEIVED.clear()

            data = stream.read(self.CHUNK, exception_on_overflow=False)
            try:
                ws.send(data, ABNF.OPCODE_BINARY)
            except:
                continue
            #print(math.sqrt(abs(audioop.avg(data, 2))) )
            if math.sqrt(abs(audioop.avg(data, 4))) > self.THRESHOLD:
                silence_chunks = 0
            else:
                silence_chunks += 1

        # Disconnect the audio stream
        stream.stop_stream()
        stream.close()

        logging.info("Done recording")

        # close the websocket
        ws.close()
        #p.terminate()

    # sleep controller for the robot.
    # wake == True, wake the robot up.
    # wake == False, put robot to sleep mode.
    def sleep(self, wake):
        if wake:
            logging.info("Exiting sleep state.")
            self.IS_SLEEPING = False
        else:
            logging.info("Entering sleep state.")
            self.IS_SLEEPING = True

    # this callback is used when the connection is activated.
    # basically initializing and configuring settings and stuff
    def on_open(self, ws):

        # dump this config dictionary out to JSON
        data = {
            "action": "start",
            "content-type": "audio/l16;rate=%d" % self.RATE,
            "continuous": True,
            "interim_results": True,
            "word_confidence": True,
            "timestamps": True,
            "max_alternatives": 3
        }

        # Send the dictionary through the socket.
        ws.send(json.dumps(data).encode('utf8'))

        # start a thread to read audio.
        threading.Thread(target=self.read_audio,
                         args=(ws, self.TIMEOUT)).start()

    # callback for when we receive a JSON message from watson.
    # egg: a useless parameter put there to avoid python yelling at me
    def on_message(self, egg, msg):

        # load json data into a multidimensional list
        data = json.loads(msg)

        # are there results?
        if "results" in data:

            # no, seriously?
            if len(data["results"]) != 0:

                # are those results final?
                if data["results"][0]["final"]:

                    # Are we sleeping though
                    if self.IS_SLEEPING:
                        if ROBOT_NAME in data['results'][0]['alternatives'][0]['transcript']:
                            self.sleep(True)
                    self.FINAL.append(data)

                logging.debug(data['results'][0]['alternatives'][0]['transcript'])

            else:
                logging.warn("No speech recognized.")

        # Unblock read_audio. we are done here.
        self.FINAL_RECEIVED.set()

    # print those errors
    def on_error(self, error, idk):
        logging.error(error)

    # inform coder dude that websocket was closed
    def on_close(self, ws):
        logging.info("Websocket closed.")

    # get_phrase should not be confused with read_audio.
    # get_phrase should always be called instead of read_audio.
    # it makes the necessary re-initializations and then calls read_audio
    # itself.
    def get_phrase(self):

        # empty out the finals list of the data from last use.

        self.FINAL = []

        # connect up the websocket
        headers = {}
        headers["Authorization"] = "Basic " + base64.b64encode(
            self.userpass.encode()).decode()
        url = ("wss://stream.watsonplatform.net//speech-to-text/api/v1/recognize"
               "?model=en-US_BroadbandModel")
        self.WS = websocket.WebSocketApp(url,
                                         header=headers,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.WS.on_open = self.on_open

        self.SLEEP_TIMER = threading.Timer(self.SLEEP_AFTER*60, self.sleep, False)

        # run the websocket
        self.WS.run_forever(
            sslopt={
                "cert_reqs": ssl.CERT_NONE,
                "check_hostname": False,
                "ssl_version": ssl.PROTOCOL_TLSv1
            }
        )

        # return the parsed result
        return "".join([i['results'][0]['alternatives'][0]
                        ['transcript'] for i in self.FINAL])


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage: " + sys.argv[0] + " <username> <password> <robot name> [<timeout>]")
        sys.exit()

    elif len(sys.argv) > 4:
        StreamingSTT(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]).get_phrase()

    else:
        s = StreamingSTT(sys.argv[1], sys.argv[2], sys.argv[3])
        x = s.get_phrase()
        print(x)
        print("\n\n\n\nget_phrase can be called as much as you want.\n\n\n\n")
        s.set_threshold(800)
        s.get_phrase()
