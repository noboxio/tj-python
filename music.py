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
git config --global push.default matching

Author: Brian McGinnis and Patrick McGinnis
Date: 7/11/17
"""

import time
import os.path
from random import shuffle
import re
import glob
import vlc
import threading


class Song:
    """Song is an object that can play sound.

    plays the fileLocation sound when asked to.
    This currently uses the VLC library for python3
    TODO: REWIND, FAST FORWARD, FAST, SLOW
    """

    def __init__(self, file_location):
        """Create a Song object that requires a file name to be passed.

        fileLocation -- the location of the wave file to be played
        """
        # song is not playing
        self.playing = False
        # load the file into the vlc player
        self._load_file(file_location)

        name = os.path.basename(self.file_location)
        self.name = name.split(",")[0]

    def get_state(self):
        """Get the current state of the song.

        retuens the current state of the player from the vlc class
        """
        return(self.player.get_state())

    def _load_file(self, file_location):
        """Load a single file and create a VLC player object.

        file_location -- The relative path to the file to be played
        """
        # if the file doesn't exist raise an exception
        # TODO: change to pull all valid audio files for mplayer
        if not os.path.isfile(file_location):
            raise IOError("file:" + file_location + " does not exist")
            self.file_location = None
        else:
            self.file_location = file_location
            self.player = vlc.MediaPlayer(self.file_location)

    def _log(self, message):
        """Print the log message with the object id.

        message -- string that needs to be logged
        """
        print("|" + str(self) + "| " + str(message))

    def play(self):
        """Play the song file.

        Play the song and wait for the song to end and return nothing
        """
        if self.playing is False:
            self.player.play()
            self._log("playing")
            self.playing = True

    def stop(self):
        """Stop this playing song.

        Stop this playing song immediately by terminating the process
        and then return nothing
        """
        self.playing = False
        self.player.stop()
        self._log("stop")

    def pause(self):
        """Pause this song.

        This will pause playing the song.
        """
        if self.playing is True:
            self.playing = False
            self._log("paused")
        else:
            self.playing = True
            self._log("un-paused")

        self.player.pause()

    def speed(self, speed):
        """Change the speed of the song.

        This will change the speed of the song playing
        Currently not implemented

        speed -- the multiplier of the speed.  1 = normal
        """
        self._log("speed is not supported yet.")
        self._log("play " + str(self) + " at speed " + str(speed))

    def seek(self, change):
        """Seek to change.

        This will seek to a new point in the song
        Currently not implemented

        change -- the amount of change to occur in seconds
        """
        self._log("seek is not supported yet.")
        self._log("seek " + str(self) + " by seek " + str(change))

    def slow(self):
        """Make this song slower.

        Will make the song play slower
        Currently not implemented
        """
        self._log("slow is not supported yet.")
        self._log("play slower")
        self.speed(-10)

    def fast(self):
        """Make this song faster.

        This will make the song play faster
        Currently not implemented
        """
        self._log("fast is not supported yet.")
        self._log("play faster")
        self.speed(10)

    def __str__(self):
        """Override the system string method.

        Returns the file location
        """
        return (self.name)

    def __repr__(self):
        """Override the system repr method.

        Returns the file location
        """
        return (self.name)

    def __eq__(self, other):
        # first check to see if the other is a song object or a string
        if isinstance(other, Song):
            if self.name == other.name:
                return True
            else:
                return False
        elif isinstance(other, str):
            if self.name == other:
                return True
            else:
                return False
        else:
            raise ValueError("invalid object type for comparison")
    def __dir__(self):
        return(['play', 'stop', 'pause', 'speed', 'slow', 'fast'])



class MusicManager(threading.Thread):
    """MusicManager is basically a manager for the music objects.

    it functions as a process so that the song can be started, stopped or
    whatever whenever
    """

    def __init__(self, tj=None):
        """Create a MusicManager type.

        doesn't require a song to be passed any more.
        """
        threading.Thread.__init__(self)
        self.tj = tj
        self.playlist = list()
        self.now_playing = None

        self.last_song = None
        self.play_once = False

    def _log(self, message):
        """Print the log message with the object id.

        message -- string that needs to be logged
        """
        print("|" + str(self) + "| " + str(message))

    def run(self):
        """Run method to be run as thread."""
        # Check to see if the song list is empty, if so then load the music
        # from the music resources folder
        if len(self.playlist) <= 0:
            self.load_music()

        while(True):
            time.sleep(1)
            if self.now_playing is not None:
                state = self.now_playing.get_state()
                if str(state) == "State.Ended":
                    self._log("song finished")
                    self.next()

    def load_music(self):
        """Load the songs that are in the resources/music folder.

        Loads the music from the resources/music folder
        """
        # TODO:change to pull all valid audio files for vlc?
        files = glob.glob("./resources/music/*.mp3")
        for f in files:
            self.load_song(Song(f))

    def load_song(self, song):
        """Load a song into the player.

        song -- song object to be added to the player
        TODO: CHECK THAT A SOUND OBJECT IS PASSED
        """
        self.playlist.append(song)
        self._log("SONG LOADED: " + str(song))
        self.last_song = song

    def add(self, song):
        """Alternate command for load_song.

        song -- song object to be added to the player.
        """
        self.load_song(song)

    def shuffle(self):
        """Shuffle the list of music objects.

        shuffles the list of music objects, it does not reset current playing.
        """
        shuffle(self.playlist)
        self.load_song(self.playlist.pop())

    def play_song_name(self, song_name):
        """Play a song based on the song name.

        Search the playlist for the song name and then play it.
        """
        # first stop playing if anything is playing
        self.stop()

        for i in range(0, len(self.playlist)):
            t = self.playlist[i]
            if t.name == song_name:
                t = self.playlist.pop(i)
                self.load_song(t)
                break


        self.play_once = True
        self.play()



    def play(self):
        """Play next song.

        Plays the next song in the list of music, if no song is playing.
        """
        # play next song if nothing is playing
        if self.now_playing is None:
            self.now_playing = self.playlist.pop(0)
            self.now_playing.play()
        else:
            self.now_playing.play()

    def stop(self):
        """Stop the song.

        Stops the song that is currently playing.
        """
        if self.now_playing is None:
            self._log("Nothing to Stop")
        else:
            self.now_playing.stop()
            self.playlist.insert(0, self.now_playing)
            self.now_playing = None

    def pause(self):
        """Pause the now_playing song.

        Pauses the now_playing song.
        """
        if self.now_playing is None:
            self._log("Nothing to Pause")
        else:
            self.now_playing.pause()

    def next(self):
        """Play next song.

        Plays the next song in the list.
        """
        self.now_playing.stop()
        self.playlist.append(self.now_playing)

        # check to see if it is the last song,
        # if so say so otherwise play the next song
        if self.now_playing == self.last_song:
            self._log("all songs in playlist played.  press play again")
            self.now_playing = None
        else:
            self.now_playing = None
            self.play()

    def previous(self):
        """Play previous song.

        Plays the previous song in the list.
        """
        self.now_playing.stop()
        self.playlist.insert(0, self.now_playing)
        self.now_playing = self.playlist.pop()
        self.now_playing.play()
        # self.playlist.

    def get_playlist(self):
        """Get playlist.

        Returns the list of songs in the playlist.
        """
        for i in self.playlist:
            print(i)
        #return(self.playlist)

    def say_playlist(self):
        if self.tj is not None:
            self.tj.watsonServices.tts.speak(self.get_playlist())

    # this needs to interpret commands JUST for the music manager
    def execute_command(self, command):
        """Execute a command in text form."""
        self._log("music execute method: " + command)
        # first check to see if the command is a manager command
        # take the command passed and just pull the method name, basically
        # remove the ().  ex. play() --> play  |  load(something) --> load

        # generate a regex
        regex = re.compile(r"^\w+")   # selects just the first word
        command_method = regex.match(command).group()
        self._log("command_method: " + command_method)

        # check to see if the command is in the managergit
        # config --global push.default matching

        if command_method in dir(self):
            # matching command was foudn
            self._log("matching command found")
            self._log("self." + command)
            eval("self." + command)
        else:
            self._log("no matching command found in MusicManager")
            if self.now_playing is None:
                self._log("MUSIC MANAGER: no song is currently playing")
            else:
                eval("self.now_playing." + command)
    def __dir__(self):
        return(['play', 'stop', 'get_playlist', 'load_music', 'play_song_name', 'say_playlist', 'next', 'previous', 'pause', 'shuffle'])
