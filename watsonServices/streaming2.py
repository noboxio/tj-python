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


streaming.py: Continuous, streaming Speech-To-Text using websockets.

Author: Brandon Gong
Date: 7/31/17
"""

import pyaudio
import threading

class SpeechToText(object):

    _chunk = 16384
    _format = pyaudio.paInt16
    _channels = 1
    _rate = 48000
    _final_phrase = []
    _threshold = 1500
    _silence_limit = 2
    _sleep_after = 300

    def _do_nothing(): pass
    def _verify_function(self, function):
        if isinstance(function, (types.FunctionType, types.LambdaType)):
            return function
        elif function is None:
            return self._do_nothing
        else:
            self._on_error_callback("Invalid parameter to be set as callback")
            return self._do_nothing

    def __init__(username, password):
        self.credentials = ":".join((username, password))
        self._on_init_begin_callback = self._do_nothing
        self._on_init_complete_callback = self._do_nothing
        self._on_sleep_callback = self._do_nothing
        self._on_wake_callback = self._do_nothing
        self._on_phrase_callback = self._do_nothing
        self._on_info_callback = lambda info : print(info)
        self._on_error_callback = lambda error : print(error, file=sys.stderr)
        self._on_cleanup_begin_callback = self._do_nothing
        self._on_cleanup_complete_callback = self._do_nothing

    def set_on_init_begin(function):
        self._on_init_begin_callback = _verify_function(function)

    def set_on_init_complete(function):
        self._on_init_complete_callback = _verify_function(function)

    def set_on_sleep(function):
        self._on_sleep_callback = _verify_function(function)

    def set_on_wake(function):
        self._on_wake_callback = _verify_function(function)

    def set_on_phrase(function):
        self._on_phrase_callback = _verify_function(function)

    def set_on_info(function):
        self._on_info_callback = _verify_function(function)

    def set_on_error(function):
        self._on_error_callback = _verify_function(function)

    def set_on_cleanup_begin(function):
        self._on_cleanup_begin_callback = _verify_function(function)

    def set_on_cleanup_complete(function):
        self._on_cleanup_complete_callback = _verify_function(function)

    def set_chunk(self, chunk):
        self._chunk = chunk

    def get_chunk(self):
        return self._chunk

    def set_format(self, paformat):
        self._format = paformat

    def get_format(self):
        return self._format

    def set_rate(self, rate):
        self._rate = rate

    def get_rate(self):
        return self._rate

    def set_threshold(self, threshold):
        self._threshold = threshold

    def get_threshold(self):
        return self._threshold

    def set_silence_limit(self, silence_limit):
        self._silence_limit = silence_limit

    def get_silence_limit(self):
        return self._silence_limit

    def set_sleep_after(self, sleep_after):
        self._sleep_after = sleep_after

    def get_sleep_after(self):
        return self._sleep_after

    def _auto_threshold(self, samples=10, avgintensities=0.1, padding=0):
        threading.Thread(target=self._on_info_callback,
                         args=("Starting auto_threshold")).start()
        stream = self._pa.open(
            format=self._format,
            channels=self._channels,
            rate=self._format,
            input=True,
            frames_per_buffer=self._chunk)
        intensities = [math.sqrt(abs(audioop.avg(stream.read(self._chunk), 4)))
                      for x in range(samples)]
        intensities = sorted(intensities, reverse=True)
        self._threshold = sum(intensities[:int(samples * avgintensities)]) / int(samples * avgintensities) + padding
        stream.close()
        threading.Thread(target=self._on_info_callback,
                         args=("Threshold: {}".format(self._threshold))).start()

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

    def on_message(self, egg, msg):
        data = json.loads(msg)
        if "results" in data:
            if len(data["results"]) != 0:
                if data["results"][0]["final"]:
                    self.FINAL.append(data)

            logging.debug(data['results'][0]['alternatives'][0]['transcript'])

    def on_error(self, error, egg):
        threading.Thread(target=self._on_error_callback, args=error).start()

    # TODO: Change auto_threshold to true by default once it is stabilized
    def init(auto_threshold=False):
        threading.Thread(target=self._on_init_begin_callback).start()
        self._pa = pyaudio.PyAudio()
        self._sleep_timer = threading.Timer(self._sleep_after, sleephandler)
        if auto_threshold: self._auto_threshold()
        headers = {}
        headers["Authorization"] = "Basic " + base64.b64encode(
            self.userpass.encode()).decode()
        url = ("wss://stream.watsonplatform.net//speech-to-text/api/v1/recognize"
               "?model=en-US_BroadbandModel")
        self._ws = websocket.WebSocketApp(url,
                                         header=headers,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self._ws.on_open = self.on_open
        threading.Thread(target=self._on_init_complete_callback).start()

    def run_forever():
        self._sleep_timer.start()
        self._ws.run_forever(
            sslopt={
                "cert_reqs": ssl.CERT_NONE,
                "check_hostname": False,
                "ssl_version": ssl.PROTOCOL_TLSv1
            }
        )
