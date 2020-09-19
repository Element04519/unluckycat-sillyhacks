from time import sleep
import speech_recognition as sr
import mapper

import RPi.GPIO as GPIO

LIGHT_GPIO = 5

def count_keyword_usage(recognized, keys):
	counting = dict()

	for entry in recognized:
		text = entry['transcript']
		current_counting = dict()

		for word in text.split(' '):
			if word.lower() in mapper.word_dict:
				if not word in current_counting:
					current_counting[word] = 0

				current_counting[word] += 1

		for word in current_counting.keys():
			if not word in counting:
				counting[word] = 0

			counting[word] = max(current_counting[word],counting[word])

	return counting




def word_listening_callback(_, audio):
	try:
		result = r.recognize_google(audio, show_all=True)
		print(result)

		if result == []:
			return

		result_by_words = count_keyword_usage(result['alternative'], mapper.word_dict.keys())
		print(result_by_words)
		
		for word in result_by_words:
			for i in range(result_by_words[word]):
				mapper.keyword_found(word)
	
	except sr.UnknownValueError:
	    print("Google could not understand audio")
	except sr.RequestError as e:
	    print(" error; {0}".format(e))


def light_sensor_callback():
	if GPIO.input(LIGHT_PIN):
		mapper.light_turned_off()
	else:
		mapper.light_turned_on()



## Start listening to words
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
	r.adjust_for_ambient_noise(source)

r.listen_in_background(mic, word_listening_callback)

## Start listening to light sensor

GPIO.setmode(GPIO.BCM) #GPIO Nr (GPIO.setmode(GPIO.BOARD) for Pin Nr)
GPIO.setup(LIGHT_PIN, GPIO.IN)

GPIO.add_event_detect(LIGHT_PIN, GPIO.BOTH, callback=light_sensor_callback)



## Don't stop waiting. Ever.

while True:
	sleep(20)
	mapper.trigger_20_sec()

