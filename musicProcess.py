"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio

Author: Brian McGinnis and Patrick McGinnis
Date: 6/23/17
"""

import time
from multiprocessing import Process
import music


class MusicProcess():

    def __init__(self, music):
        self.music = music
        self.process = None

    def play(self):
        self.__clearProcess__()
        self.process = Process(target=self.music.play)
        self.process.start()

    def stop(self):
        self.__clearProcess__()
        self.process = Process(target=self.music.stop)
        self.process.start()

    def __clearProcess__(self):
        if self.process is not None:
            self.process.terminate()
