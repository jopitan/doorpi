import RPi.GPIO as GPIO
import atexit
from time import sleep
import sys

switchPin = 7

GPIO.setmode(GPIO.BOARD)

if GPIO.gpio_function(switchPin) == 0:
    sys.exit()

GPIO.setup(switchPin, GPIO.OUT)
GPIO.output(switchPin, True)
sleep(float(sys.argv[1]))
GPIO.output(switchPin, False)
GPIO.cleanup()
