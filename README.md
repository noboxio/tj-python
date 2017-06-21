# tj-python

## IBM's TJBot code rewritten in Python.

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
