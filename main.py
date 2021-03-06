from time import sleep
import speech_recognition as sr
import mapper
import output

#import sounddevice as sd
import numpy as np
import RPi.GPIO as GPIO

LIGHT_GPIO = 5
def count_keyword_usage(recognized, keys):
    counting = dict()

    for entry in recognized:
        text = entry['transcript']
        current_counting = dict()

        for word in text.lower().split(' '):
            if word.lower() in mapper.keyword_dict:
                if not word in current_counting:
                    current_counting[word] = 0

                current_counting[word] += 1

        for word in current_counting.keys():
            if not word in counting:
                counting[word] = 0

            counting[word] = max(current_counting[word],counting[word])

    return counting




def word_listening_callback(_, audio):
    print("callback triggered")
    try:
        result = r.recognize_google(audio, show_all=True)
        print(result)

        if result == []:
            return

        result_by_words = count_keyword_usage(result['alternative'], mapper.keyword_dict.keys())
        print(result_by_words)
        
        mapper.keyword_found(result_by_words)
    
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print(" error; {0}".format(e))


#def light_sensor_callback():
#    if GPIO.input(LIGHT_PIN):
#        mapper.light_turned_off()
#    else:
#        mapper.light_turned_on()
    

print("try starting")

## Start listening to words
r = sr.Recognizer()
mic = sr.Microphone()

print("initialized")

with mic as source:
    r.adjust_for_ambient_noise(source)

r.listen_in_background(mic, word_listening_callback)
print("started listening")
## Start listening to light sensor

GPIO.setmode(GPIO.BCM) #GPIO Nr (GPIO.setmode(GPIO.BOARD) for Pin Nr)
GPIO.setup(LIGHT_GPIO, GPIO.IN)

#GPIO.add_event_detect(LIGHT_PIN, GPIO.BOTH, callback=light_sensor_callback)

def get_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    mapper.process_sound(int(volume_norm))

#with sd.Stream(callback=get_sound):
  ## Don't stop waiting. Ever.

count = 0
goal = 300
output.start_pwm()
light_was_on = False

while True:
    sleep(0.1)
    output.reset_pwm()
    count += 1
    
    if count >= goal:
        count = 0
        mapper.trigger_time()

    if not GPIO.input(LIGHT_GPIO): #light on now
        #print("an")
        if not light_was_on:
            mapper.light_turned_on()
            light_was_on = True
    else:
        #print("aus")
        if light_was_on:
            mapper.light_turned_off()
            light_was_on = False

