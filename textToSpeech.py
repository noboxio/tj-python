from watson_developer_cloud import TextToSpeechV1

class textToSpeech(username, password):
  
  textToSpeech = TextToSpeechV1(
    username=username,
    password=password,
    x_watson_learning_opt_out=True)
  
  def speak(message):
    texToSpeech.synthesize(message, accept = audio/wav', voice="en-US_AllisonVoice")
    
