#conding:utf-8
#import sounddevice
#from scipy.io.wavfile import write
#import audiofile
import speech_recognition as sr
import pyttsx3 as tts
'''
import pandas as pd
import quandl

df=quandl.get('WIKI/GOOGL')
df=f[[ 'Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
print(df.head())

'''
'''
def generateMP3():
	import pyttsx3 as tts

	sound='name.mp3'

	engine=tts.init()

	engine.save_to_file('didier fait pipi au lit', sound)

	engine.runAndWait()

	return sound

'''
'''
fr=44100
sec=int(input('temps du rec :'))
print('rec en cours')
record=sounddevice.rec(int(sec*fr),samplerate=fr,channels=2)
sounddevice.wait()
write('son.mp3',fr,record)
'''
'''
sound=generateMP3()

r=sr.Recognizer()
with  sr.AudioFile(sound) as source:
#with  sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print('file is beens analyse:')
	#audio=r.listen(source)
	audio=r.record(source)
	try:
		txt=r.recognize_google(audio)
		print('text:{txt}')
		textfile=open('speech.text','a')
		textfile.writelines(txt)
	except Exception as e:
		print(e)


with open('sound.wav', 'wb') as t:
		t.write(audio.get_wav_data())
		'''
r=sr.Recognizer()

while True:
	try:
		with  sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio=r.listen(source)
			text=r.recognize_google(audio, language="fr-FR")
			text=text.lower()
			print(text)
			textfile=open('speech.txt','a')
			textfile.writelines(text)
	except Exception as e:
		r=sr.Recognizer()
		print(e)
		continue