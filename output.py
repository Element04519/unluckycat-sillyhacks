#import hardware
import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)



def set_led(level = 0): #0,1,2,3,4
	#print("Setting led...")
        s = serial.Serial('/dev/ttyUSB0', 9600)
        s.open()
        time.sleep(5)
        s.write(str(level).encode())
        s.close()

def set_arm(level = 0): #0,1,2,3
	#print("Setting arm...")
        arm = GPIO.PWM(12, 1000)
        arm.start(100)
        time.sleep(0.2)
        if level == 0:
            arm.ChangeDutyCycle(0)
        if level == 1:
            arm.ChangeDutyCycle(35)
        if level == 2:
            arm.ChangeDutyCycle(70)
        if level == 3:
            arm.CHangeDutyCycle(100)
            
def set_puke(level = 0): #0,1
	#print("Setting puke...")
        if level == 0:
            GPIO.output(13, GPIO.LOW)
        else:
            GPIO.output(13, GPIO.HIGH)

def shout():
	print("Bullshit!")

def beep():
	print("Beep!")
