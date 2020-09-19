from time import sleep
import speech_recognition as sr
import mapper

def callback(_, audio):
	try:
		result = r.recognize_google(audio)
		print(result)
		
		for word in result.split(' '):
			mapper.process_word(word)
	
	except sr.UnknownValueError:
	    print("Sphinx could not understand audio")
	except sr.RequestError as e:
	    print(" error; {0}".format(e))

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
	r.adjust_for_ambient_noise(source)

r.listen_in_background(mic, callback)

while True:
	sleep(20)
	mapper.trigger_20_sec()
