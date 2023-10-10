'''import speech_recognition as sr

sound='name.mp3'

r=sr.Recognizer()

with  sr.AudioFile(sound) as source:
	r.adjust_for_ambient_noise(source)
	print('please say something:')
	audio=r.listen(source)
	try:
		print('converting audio is :n'+ r.recognize_google(audio))
	except Exception as e:
		raise Exception('Invalid : {}'.format(e))
	


	#with open('sound.wav', 'wb') as t:
		#t.write(audio.get_wav_data())
		

import pyttsx3 as tts

engine=tts.init()
engine.save_to_file(sound)
engine.runAndwait()
	
from translate import Translator
to_lang = 'zh'
secret = 'your secret from Microsoft or DeepL'
translator = Translator(provider='libre', to_lang=to_lang, secret_access_key=secret)
translator.translate(secret)
'''
import speech_recognition as sr


def generateMP3():
	#import pyttsx3 as tts
	#from googletrans import Translator
	from gtts import gTTS
	import os

	sound='name.mp3'

	#translator = Translator()
	#engine=tts.init()

	with open('speech.txt','r') as f:
		#flines = f.readlines()
		flines = f.read()
		langs='fr'
		textspeech=gTTS(text=flines,lang=langs,slow=False)
		textspeech.save(sound)
		os.popen(sound)
		#out=translator.translate(flines, dest='en')
		#engine.save_to_file(out.text, sound)

		#engine.runAndWait()

	return sound







sound=generateMP3()
'''
r=sr.Recognizer()
with  sr.AudioFile(sound) as source:
#with  sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print('file is beens analyse:')
	#audio=r.listen(source)
	audio=r.record(source)
	try:
		txt=r.recognize_google(audio)
		#textfile=open('speech.txt','a')
		#textfile.writelines(out)
	except Exception as e:
		print(e)
		'''
