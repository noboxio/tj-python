# Differences in this library compared to others
  * We don't use conflicting pins.  We use software PWM for the servo and we use the SPI buss for the LED instead of using the 2 default PWM ports that are used for left and right audio.
  * We use analog audio to a speaker and use a different microphone than the small micro one everyone uses.  It has significantly better pickup for the cost difference.

![alt text][wiring-diagram]

[wiring-diagram]: https://cdn.rawgit.com/noboxio/tj-python/4d967c93/config/raspberryPiTJ.svg "Wiring Diagram"


**THINGS THAT HAVE TO BE PERFORMED ON A NEW PI**
 1. Download the newest Raspbian image from: https://www.raspberrypi.org/downloads/raspbian/
    * We currently use RASPBIAN JESSIE WITH DESKTOP 2017-07-05
 2. Load the downloaded .img file onto your SD card.  Raspberry Pi recommends that you use Etcher.  See their Installing Operating Systems Images page: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

 1. Configure the Raspberry Pi
      * Raspberry Icon --> Preferences --> Raspberry Pi Configuration
          * System:
            * Underscan: Disabled
          * Interfaces:
            * Camera: Enabled
            * SSH: Enabled
            * Serial: Enabled
          * Performance:
            * GPU Memory: 256
          * Localisation:
            * Locale: *click Set Locale...*
              * Language: en (English)
              * Country: US (USA)
            * Timezone: *click Set Timezone...*
              * Area: US
              * Location: Central
            * Keyboard: *click Set Keyboard...*
              * Country: United States
              * Variant: English (US)  *scroll up to see it at the top*
      * Then reboot the pi `sudo reboot` or use the menu
 2. Set the default audio to be analog audio.  `sudo raspi-config`
    * Pick option `7 Advanced Options`
    * Pick option `A4 Audio`
    * Pick option `1 Force 3.5mm ('headphone') jack`
    * Press the Enter Key
    * Use the Left and Right arrow keys to select `<Finish>` and press the Enter Keyboard



#Then you can run the script located in config/setup.sh or you can execute the commands manually below.

   1. Update the dist list: `sudo apt-get update`
   1. Upgrade the apps `sudo apt-get upgrade`
      * Tell is yes if it asks if you want to continue `Y`
   1. Upgrade the distro `sudo apt-get dist-upgrade`
   1. Install vim `sudo apt-get install vim`
      * Vim config TODO
      * Git config use vim TODO
   1. REMOVE Install screen `sudo apt-get install screen`
   1. Install Python 3 and set as default
      * Already default
   1. Install system dependencies they are found on the pyaudio page(Below)
      * `sudo apt-get install portaudio19-dev`
      * `sudo apt-get install python-all-dev`
      * `sudo apt-get install python3-dev`
      * `sudo apt-get install python3-pyaudio python-pyaudio`  !!!THIS DOES NOT WORK ON THE RPi!!!
      * TODO: Need to add the special code from the non standard dist that makes PyAudio work.   This may not be correct if the new library doesn't require it!
   1. Install system dependencies for the watson-developer-cloud
      * `sudo apt-get install libssl-dev libffi-dev build-essential scons swig`
      * `sudo easy_install3 --upgrade watson-developer-cloud`
   1. Install the adafruit stuff  
      * `sudo pip3 install RPi.GPIO`
   1. Install this for the LED controls
      * `git clone https://github.com/jgarff/rpi_ws281x.git`
      * `cd rpi_ws281x`
      * `scons`
      * `cd python`
      * `sudo python3 setup.py install`
   1. You need to copy the asound.conf file to /etc/
      * `sudo cp asound.conf /etc/asound.conf`
   1. You need to copy the asound file to ~/.asound
      * `cp .asoundrc ~/.asoundrc`
   1. Install VLC to play the music
      * `sudo apt-get install vlc`
   1. Install the python libraries required.
      * `sudo easy_install3 websocket-client`
      * `sudo pip3 install colour`
      * `sudo pip3 install python-vlc`

Thinking about adding:
`sudo pip3 install SpeechRecognition`




# IBM's TJBot code rewritten in Python.
*__NEEDS TO BE UPDATED__*

*__This is initial infromation that somewhat applies to the code in this repository but it is not up to date at this time.__*

  * Things we want to be able to do in python:  
  * Speech to text, preferably more live than waiting for no sound to process, but whatever  
  * Again need to figure out how to add some keywords to his vocabulary  
  * Function waitforsomething(resetafter)   
  * Maybe if it keeps hearing something after a while it says idk how to help  
  * Text to speech, make sure you can do the character inflection and verbal tone stuff with taht one female voice.  
    * Function speak(text) maybe speak(text, emotion)  
  * Conversation, send text to the conversation module and have it return a string, possibly with inflection or some kind of string at the beginning [wave] where [] denotes a command and the inside is a command that TJ bot will process and do and then remove it before it speaks it or something.  
    * Function sendconversation(conversation), will wait for a response  
  * Tone analysis, send the text from speech to text through the tone to add some context for the conversation part.  Figure out how    to use the context stuff in teh conversation stuff.  
    * Function analyzetone(text), returns the emotion array  
    * Function analyzetonesimple(text), returns the highest option. Ex “sad”  
  * This Personality thing, no idea what it is.  

## Servo  
  Function wave(duration) or wave(count)  
  Function setangle(angle) or setangle(angle, speed)  
  Function up(), down(), forward() ---> just sends an angle to the set angle function  
  Function stop()  


## LED  
  Function setcolor(r,g,b) or setcolor(hex) or setcolor(color)  
  Function playsequence(sequence)  
  Sequence is a list of actions  
  A sequence has a repeat infinite, repeat count options   
  An action for the LED has a color and a duration  
  Function rainbow(speed) → does stuff with colors  
  Function strobe(speed) → strobes white at the speed  
  Function stop()  

## Music  
  Function playmusic(sound file)  
  Function volup(), voldown(), volmute()  
  Function pause(), stop(), restart()  


## Camera  
  Take a picture and just show it on the screen  
  Show a live video stream  
