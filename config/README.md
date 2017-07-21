***INSTRUCTIONS***

**THINGS THAT HAVE TO BE DONE**

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

2. Update the dist list: `sudo apt-get update`

3. Upgrade the apps `sudo apt-get upgrade`
    * Tell is yes if it asks if you want to continue `Y`

4. Upgrade the distro `sudo apt-get dist-upgrade`

5. Install vim `sudo apt-get install vim`
    * Vim config TODO
    * Git config use vim TODO

6. REMOVE Install screen `sudo apt-get install screen`

7. Install Python 3 and set as default
    * Already default

8. Install system dependencies they are found on the pyaudio page(Below)
    * `sudo apt-get install portaudio19-dev`
    * `sudo apt-get install python-all-dev`
    * `sudo apt-get install python3-dev`
    * `sudo apt-get install python3-pyaudio python-pyaudio`

9. Install system dependencies for the watson-developer-cloud
    * `sudo apt-get install libssl-dev libffi-dev build-essential scons swig`
    * `sudo easy_install3 --upgrade watson-developer-cloud`
        * This one takes a while and seems like it stalls, but just let it run!

10. Install the adafruit stuff  
    * `sudo pip3 install RPi.GPIO`

11. Install this for the LED controls
    * `git clone https://github.com/jgarff/rpi_ws281x.git`
    * `cd rpi_ws281x`
    * `scons`
    * `cd python`
    * `sudo python3 setup.py install`

12. You need to copy the asound.conf file to /etc/
    * `cp asound.rc /etc/asound.rc`

13. You need to copy the asound file to ~/.asound
    * `cp .asoundrc ~/.asoundrc`

14. Install VLC to play the music
    * `sudo apt-get install vlc`

14. Install the python libraries required.
    * `sudo easy_install3 websocket-client`
    * `sudo pip3 install colour`
    * `sudo pip3 install python-vlc`
