#!/usr/bin/env python.

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
Date: 7/11/17
atom-timestamp:update-timestamp
"""

import time
import subprocess
from multiprocessing import Process



class Music:
    """Music is an object that can play sound.

    plays the fileLocation sound when asked to
    """

    def __init__(self, fileLocation):
        """Create a Music object that requires a file name to be passed.

        fileLocation -- the location of the wave file to be played
        """
        self.fileLocation = fileLocation
        self.cmd = "aplay " + fileLocation

    def play(self):
        """Play the song file.

        Play the song and wait for the song to end and return nothing
        """
        self.process = subprocess.Popen("exec " + self.cmd,
                                        stdout=subprocess.PIPE, shell=True)

    def stop(self):
        """Stop this playing song.

        Stop this playing song immediately by terminating the process
        and then return nothing
        """
        self.process.kill()





class MusicManager():
    """MusicManager is basically a manager for the music objects.

    it functions as a process so that the song can be started, stopped or
    whatever whenever
    """

    def __init__(self, music):
        """Create a MusicManager type.

        music -- Music object that has been created to be played

        TODO: don't require it to be passed a song, allow it to load a
        library of songs.
        """
        self.music = music
        self.process = None


    def execute_command(self, command):
        """Execute a command in text form"""
        self.__clearProcess__()
        self.process = Process(target=eval("self.music." + command))
        self.process.start()


    def __clearProcess__(self):
        """Clear any exisiting Music process so that it can be terminated."""
        if self.process is not None:
            self.process.terminate()
