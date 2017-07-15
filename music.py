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
import glob
import vlc
import threading

class Song:
    """Song is an object that can play sound.

    plays the fileLocation sound when asked to.
    TODO: REWIND, FAST FORWARD, FAST, SLOW
    """

    def __init__(self, file_location):
        """Create a Song object that requires a file name to be passed.

        fileLocation -- the location of the wave file to be played
        """
        #song is not playing
        self.playing = False

        self._load_file(file_location)

    def get_state(self):
        return(self.player.get_state())

    def _load_file(self, file_location):
        #if the file doesn't exist raise an exception
        #TODO: change to pull all valid audio files for mplayer
        if not os.path.isfile(file_location):
            raise IOError("file:" + file_location + " does not exist")
            self.file_location = None
        else:
            self.file_location = file_location
            self.player = vlc.MediaPlayer(self.file_location)

    def play(self):
        """Play the song file.

        Play the song and wait for the song to end and return nothing
        """
        #self.process = subprocess.Popen("exec " + self.cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        if self.playing is False:
            self.player.play()
            self.playing = True

    def stop(self):
        """Stop this playing song.

        Stop this playing song immediately by terminating the process
        and then return nothing
        """
        self.playing = False
        self.player.stop()

    def pause(self):
        """Pause this song.

        This will pause playing the song.
        """
        if self.playing is True:
            self.playing = False
        else:
            self.playing = True

        self.player.pause()

    def speed(self, speed):
        print("play " + str(self) + " at speed " + str(speed))

    def seek(self, change):
        print("seek " + str(self) + " by seek " + str(seek))

    def slow(self):
        print("play slower")
        self.speed(-10)

    def fast(self):
        print("play faster")
        self.speed(10)

    def __str__(self):
        return (self.file_location)



class MusicManager(threading.Thread):
    """MusicManager is basically a manager for the music objects.

    it functions as a process so that the song can be started, stopped or
    whatever whenever

    TODO: NEXT, PREVIOUS
    """

    def __init__(self):
        """Create a MusicManager type.

        doesn't require a song to be passed any more.
        """
        threading.Thread.__init__(self)
        self.process = None
        self.playlist = list()
        self.now_playing = None

        #self.process = Process(target=self._check_status)
        #self.process.start()
        self.start()

    def run(self):
        while(True):
            time.sleep(1)
            if self.now_playing is None:
                msg = "no song playing"
            else:
                msg = self.now_playing.get_state()
            print("_check_status: " + str(msg))

    def load_music(self):
        """Load the songs that are in the resources/music folder

        """
        #TODO: change to pull all valid audio files for mplayer DO THIS INSIDE OF SONG
        files = glob.glob("./resources/music/*.wav")
        for f in files:
            self.load_song(Song(f))

    def load_song(self, song):
        """Load a song into the player

        song -- song object to be added to the player
        TODO: CHECK THAT A SOUND OBJECT IS PASSED
        """
        self.playlist.append(song)
        print("SONG LOADED: " + str(song))

    def add(self, song):
        """Alternate command for load_song.

        song -- song object to be added to the player
        """
        self.load_song(song)

    def shuffle(self):
        """Shuffle the list of music objects

        shuffles the list of music objects, it does not reset current playing
        """
        shuffle(self.playlist)

    def play(self):
        #play next song if nothing is playing
        if self.now_playing == None:
            self.now_playing = self.playlist.pop(0)
            self.now_playing.play()
        else:
            self.now_playing.play()

    def stop(self):
        self.now_playing.stop()
        self.playlist.insert(0, self.now_playing)
        self.now_playing = None

    def pause(self):
        if self.now_playing == None:
            print("Nothing to Pause")
        else:
            self.now_playing.pause()

    def next(self):
        self.now_playing.stop()
        self.playlist.append(self.now_playing)
        self.now_playing = None
        self.play()

    def previous(self):
        self.now_playing.stop()
        self.playlist.insert(0, self.now_playing)
        self.now_playing = self.playlist.pop()
        self.now_playing.play()
        #self.playlist.

    def get_playlist(self):
        return(self.playlist)





    #this needs to interpret commands JUST for the music manager
    def execute_command(self, command):
        """Execute a command in text form"""

        print("music execute method: " + command)
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
            print("self." + command)
            eval("self." + command)
        else:
            print("no matching command found in MusicManager")
            if self.now_playing is None:
                print("MUSIC MANAGER: no song is currently playing")
            else:
                eval("self.now_playing." + command)






    def __clearProcess__(self):
        """Clear any exisiting Music process so that it can be terminated."""
        if self.process is not None:
            self.process.terminate()
