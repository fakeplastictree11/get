import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
n = 8
levels = 2 ** n
max_voltage = 3.236
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)
adc_value = 0
adc_values = []
counter = 1
experiment_start = time.time()

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    result = 0
    weight = levels // 2
    for i in range(n):
        GPIO.output(dac, decimal2binary(result + weight))
        time.sleep(0.01)
        if (GPIO.input(comp) == 1):
            result += weight
        weight //= 2       
    return result

try:
    while (adc_value < 247):
        adc_value = adc()
        adc_values.append(adc_value)
        voltage = adc_value * max_voltage / levels
        print("Значение на АЦП: {}, напряжение на конденсаторе: {:.3f}, номер измерения: {}".format(adc_value ,voltage, counter))
        for i in range((adc_value + 31) // 32):
            GPIO.output(leds[i], 1)
        for i in range((adc_value + 31) // 32, n):
            GPIO.output(leds[i], 0)
        counter += 1    
    GPIO.output(troyka, 0)
    while (adc_value > 5):
        adc_value = adc()
        adc_values.append(adc_value)
        voltage = adc_value * max_voltage / levels
        print("Значение на АЦП: {}, напряжение на конденсаторе: {:.3f}, номер измерения: {}".format(adc_value ,voltage, counter))
        for i in range((adc_value + 31) // 32):
            GPIO.output(leds[i], 1)
        for i in range((adc_value + 31) // 32, n):
            GPIO.output(leds[i], 0)
        counter += 1
    experiment_finish = time.time()
    experiment_duration = experiment_finish - experiment_start
    plt.plot(adc_values, color='g')
    plt.title('Зависимость значений на АЦП от номера измерения')
    plt.xlabel('Номер измерения')
    plt.ylabel('Значение на АЦП')
    plt.grid()
    plt.show()
    adc_values_string = [str(item) for item in adc_values]

    with open('data.txt', 'w') as data:
        data.write("\n".join(adc_values_string))
    with open('settings.txt', 'w') as settings:
        settings.write("{:.3f}\n{:.3f}".format(counter / experiment_duration, max_voltage / levels))
    print()
    print()
    print("Продолжительность эксперимента (с): {:.3f}".format(experiment_duration))
    print("Период одного измерения (с): {:.3f}".format(experiment_duration / counter))
    print("Частота дискретизации измерений (Гц): {:.3f}".format(counter / experiment_duration))
    print("Шаг квантования (В): {:.3f}".format(max_voltage / levels))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()