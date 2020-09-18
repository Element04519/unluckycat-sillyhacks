from time import sleep
import speech_recognition as sr
import mapper


def callback(_, audio):
	try:
	    result = r.recognize_sphinx(audio, keyword_entries=KEYWORDS)
	    for word in result.split(' '):
	    	mapper.word_found(word)

	except sr.UnknownValueError:
	    print("Sphinx could not understand audio")
	except sr.RequestError as e:
	    print("Sphinx error; {0}".format(e))




KEYWORDS = mapper.get_keywords()
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
	r.adjust_for_ambient_noise(source)

r.listen_in_background(mic, callback)

while True:
	sleep(0.1)
