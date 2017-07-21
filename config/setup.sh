
echo Installing Port Audio Stuff.
sudo apt-get install portaudio19-dev
sudo apt-get install python-all-dev
sudo apt-get install python3-dev
sudo apt-get install python3-pyaudio python-pyaudio

echo Installing stuff for the watson cloud connectors.
echo This one takes a while and seems like it stalls, but just let it run!
sudo apt-get install libssl-dev libffi-dev build-essential scons swig
sudo easy_install3 --upgrade watson-developer-cloud


echo Installing the RPi GPIO stuff
sudo pip3 install RPi.GPIO

echo Install the Adafruit Led software
cd ~/
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python3 setup.py install

echo Copying the confil files for asound
cp asound.rc /etc/asound.rc
cp .asoundrc ~/.asoundrc

echo Install VLC
sudo apt-get install vlc

echo Install the required Python3 Libraries
sudo easy_install3 websocket-client
sudo pip3 install colour
sudo pip3 install python-vlc
