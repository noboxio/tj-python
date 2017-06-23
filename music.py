"""
Author: Brian McGinnis
"""

import time
import subprocess

class Music:

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.cmd = "aplay " + fileLocation

    def play(self):
        self.process = subprocess.Popen("exec " + self.cmd, stdout=subprocess.PIPE, shell=True)

    def stop(self):
        self.process.kill()

    
