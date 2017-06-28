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
    """ MusicProcess is basically a manager for the music objects, it functions
        as a thread so that the song can be started, stopped or whatever whenever"""

    def __init__(self, music):
        """ Constructor for the MusicProcess type, it requires a music objects
            music -- Music object that has been created to be played

            TODO: don't require it to be passed a song, allow it to load a
            library of songs."""
        self.music = music
        self.process = None

    def play(self):
        """ Plays the single song and then immediately returns nothing"""
        self.__clearProcess__()
        self.process = Process(target=self.music.play)
        self.process.start()

    def stop(self):
        """ Stops the single song and then immediately returns nothing"""
        self.__clearProcess__()
        self.process = Process(target=self.music.stop)
        self.process.start()

    def __clearProcess__(self):
        """ Clears any exisiting Music process so that it can be terminated"""
        if self.process is not None:
            self.process.terminate()
