"""
Author: Brian McGinnis and Patrick McGinnis
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
        self.process = Process(target = self.music.play)
        self.process.start()
                
    def stop(self):
        self.__clearProcess__()
        self.process = Process(target = self.music.stop)
        self.process.start()
        
    def __clearProcess__(self):
        if self.process != None:
            self.process.terminate()


