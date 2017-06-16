from watson_developer_cloud import TextToSpeechV1
import json

class textToSpeech(username, password):
def __init__(username, password):

  textToSpeech = TextToSpeechV1(
    username= username,
    password= password,
    x_watson_learning_opt_out=True)
  
  def speak(message):
	with open(join(dirname(__file__), '../resources/output.wav'), 'wb') as audio_file:
    		audio_file.write(
        		text_to_speech.synthesize(message, accept='audio/wav',
                                  voice="en-US_AllisonVoice"))

	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"../resources/output.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  
	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  
	#stop stream  
	stream.stop_stream()  
	stream.close()  
	#close PyAudio  
	p.terminate()  
