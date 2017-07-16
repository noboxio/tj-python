***INSTRUCTIONS***


!TODO: Brian needs to work on this list


**THINGS THAT HAVE TO BE DONE**
1. Run `raspi-config` and then:
    1. Expand file system
    2. Set gpu to 256
    3. Enable camera and other things
    4. Turn off under scan

2. Update the dist list: `sudo apt-get update`
3. Upgrade the apps `sudo apt-get upgrade`
4. Upgrade the distro `sudo apt-get dist-upgrade`

5. Install vim `sudo apt-get install vim`
    * Vim config TODO
    * Git config use vim TODO

6. Install screen `sudo apt-get install screen`

7. Install Python 3 and set as default TODO add code
8. Install system dependencies they are found on the pyaudio page(Below)
    * `Sudo apt-get install portaudio19-dev`
    * `Sudo apt-get install python-all-dev`
    * `sudo apt-get install python-pyaudio python3-pyaudio`

9. Install system dependencies for the watson-developer-cloud
    * `sudo apt-get install libssl-dev`
    * `sudo apt-get install libffi-dev`
    * `sudo easy_install3 --upgrade watson-developer-cloud`
        * needs to be changed to install for python3!
    * `sudo apt-get install build-essential python-dev scons swig`

10. Install the adafruit stuff  
    * `git clone https://github.com/jgarff/rpi_ws281x.git`
    * `cd rpi_ws281x`
    * `scons`
    * `cd python`
    * `sudo python3 setup.py install`

11. you need to copy the asound.conf file to ??? TODO: FINISH THIS

12. you need to copy the asound file to ~/.asound
    * `cp .asoundrc ~/.asoundrc`

13. Install the python libraries required.
    * sudo easy_install3 websocket-client
    * sudo pip3 install colour
    WHEN IT GETS TO THE SOCKET PART INSTALL SOCKET CLIENT NOT SOCKET OR SOMETHING LIKE THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  TODO: FINISH THIS


  14. you need to have pip install colour for the color name functions


sudo apt-get install python3-dev
  pip3 install RPi.GPIO
