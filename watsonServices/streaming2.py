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
#   - on_init: when initialization is complete
#   - on_sleep: 

# PATRICK: Consider splitting the below method into two separate methods:
#    - The __init__ constructor, maybe taking only a username and a password as
#      params, which does nothing but create a new instance,
#    - and a separate init() method, maybe taking the callback functions as
#      parameters, which creates the pyaudio instance and
#      initializes a websocket and stuff.
# Or you can do all that in the constructor as well.  I don't really have
# strong feelings about this.
def init(username, password):
    pass
