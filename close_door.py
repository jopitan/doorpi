import RPi.GPIO as GPIO
import atexit
from time import sleep
import sys

switchPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(switchPin, GPIO.OUT)
GPIO.output(switchPin, False)
GPIO.cleanup()
