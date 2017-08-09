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

# TODO:
# planned callbacks:
#   - on_init_begin(): when initialization is started
#   - on_init_complete(): when initialization is complete
#   - on_sleep(): when robot enters sleep state
#   - on_wake(): when robot exits sleep state
#   - on_phrase(phrase): when a full phrase is processed
#   - on_info(info): for logging purposes, general information.
#   - on_error(error): when error occurs
#   - on_cleanup_begin(): when cleanup is started
#   - on_cleanup_complete(): when cleanup is complete

class SpeechToText(object):

    def __init__(username, password):
        self.userpass = ":".join((username, password))
