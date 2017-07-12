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
"""

import time
import subprocess
from multiprocessing import Process
import os.path
from random import shuffle
import re




class Music:
    """Music is an object that can play sound.

    plays the fileLocation sound when asked to
    """

    def __init__(self, file_location):
        """Create a Music object that requires a file name to be passed.

        fileLocation -- the location of the wave file to be played
        """
        #if the file doesn't exist raise an exception
        if not os.path.isfile(file_location):
            raise IOError("file:" + file_location + " does not exist")
            self.file_location = None
            self.cmd = ""
        else:
            self.file_location = file_location
            self.cmd = "aplay " + file_location

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

    def __init__(self):
        """Create a MusicManager type.

        doesn't require a song to be passed any more.
        """
        self.process = None
        self.playlist = list()
        self.now_playing = None

    def load_song(self, music):
        """Load a song into the player

        music -- music object to be added to the player
        """
        self.playlist.append(music)

    def shuffle(self):
        """Shuffle the list of music objects

        shuffles the list of music objects, it does not reset current playing
        """
        shuffle(self.playlist)

    def play(self):
        #play next song
        if self.now_playing == None:
            self.now_playing = self.playlist.pop(0)
        else:
            pass
            #there is nothing to do

    def stop(self):
        self.playlist.append(self.now_playing)
        self.now_playing = None

    def pause(self):
        self.now_playing.stop()

    def resume(self):
        self.now_playing.start()

    def next(self):
        self.playlist.append(self.now_playing)
        self.now_playing = None
        self.play()

    def previous(self):
        temp = self.playlist.pop()
        #self.playlist.

    #this needs to interpret commands JUST for the music manager
    def execute_command(self, command):
        """Execute a command in text form"""

        #first check to see if the command is a manager command
        #take the command passed and just pull the method name, basically
        #remove the ().  ex. play() --> play  |  load(something) --> load

        #generate a regex
        regex = re.compile(r"^\w+") #selects just the first word
        command_method = regex.match(command).group()
        print("command_method: " + command_method)

        # check to see if the command is in the manager
        if command_method in dir(self):
            #matching command was foudn
            print("matching command found")
            self.__clearProcess__()
            self.process = Process(target=eval("self." + command))
            self.process.start()
        else:
            #maybe it is in the led object?
            print("no matching command fond")
            self.__clearProcess__()
            self.process = Process(target=eval("self.led." + command))
            self.process.start()





    def __clearProcess__(self):
        """Clear any exisiting Music process so that it can be terminated."""
        if self.process is not None:
            self.process.terminate()
