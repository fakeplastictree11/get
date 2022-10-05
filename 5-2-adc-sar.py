import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
n = 8
levels = 2 ** n
max_voltage = 3.3
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    result = 0
    weight = levels // 2
    for i in range(n):
        GPIO.output(dac, decimal2binary(result + weight))
        time.sleep(0.005)
        if (GPIO.input(comp) == 1):
            result += weight
        weight //= 2
    return result

try:
    while True:
        adc_value = adc()
        voltage = adc_value * max_voltage / levels
        print("Значение на АЦП: {}, подаваемое напряжение: {:.3f}".format(adc_value ,voltage))
          

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()