def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
period = float(input("Введите период: "))
try:
    while True:
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(period / 512)
        for i in range(255, -1, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(period / 512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
