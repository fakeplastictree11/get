import RPi.GPIO as GPIO
import time
import random

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0] * len(dac)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
for i in range(len(dac)):
    number[i] = random.randint(0, 1)
GPIO.output(dac, number)
time.sleep(2)

number = [1, 0, 0, 0, 0, 0, 0, 0]
GPIO.output(dac, number)
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()