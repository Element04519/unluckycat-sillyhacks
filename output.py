#import hardware
import RPi.GPIO as GPIO
import time
import serial
import atexit

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

s = serial.Serial('/dev/ttyUSB0', 115200)
s.close()
s.open()
while(not s.is_open):
    time.sleep(0.1)
arm = GPIO.PWM(12, 1000)

arm_level = 0
old_arm_level = 0

def safe_stop():
    arm_level = 0
    reset_pwm()

    GPIO.output(13, GPIO.LOW)
    s.write("0".encode())
    time.sleep(0.2)
    s.close()

atexit.register(safe_stop)

def set_led(level = 0): #0,1,2,3,4
    print("Setting led..."+str(level))
    s.write(str(level).encode())

def set_arm(level = 0): #0,1,2,3
    print("Setting arm..."+str(level))
    global arm_level
    arm_level = level

def start_pwm():
    arm.start(100)
    time.sleep(0.2)

def reset_pwm():
    global arm_level, old_arm_level
    val = 0

    if arm_level == 0:
        val = 0
    else:
        if old_arm_level == 0:
            arm.ChangeDutyCycle(100)
            time.sleep(0.2)
    old_arm_level = arm_level

    if arm_level == 1:
        val = 35
    if arm_level == 2:
        val = 70
    if arm_level == 3:
        val = 100
    
    arm.ChangeDutyCycle(val)
    time.sleep(0.2)


def set_puke(level = 0): #0,1
        print("Setting puke..."+str(level))
        if level == 0:
            GPIO.output(13, GPIO.LOW)
        else:
            GPIO.output(13, GPIO.HIGH)
def shout():
    print("BULLSHIT")
    pass

def beep():
    pass
