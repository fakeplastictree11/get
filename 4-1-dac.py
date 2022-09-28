def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def isnumber(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isfloat(value):
    try:
        int(value)
        return False
    except ValueError:
        return True

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        input_value = input("Введите число от 0 до 255: ")
        if input_value == 'q':
            print("Вы ввели не числовое значение. Конец.")
            break
        elif not isnumber(input_value):
            print("Вы ввели не числовое значение.")
            continue
        elif isfloat(input_value):
            print("Вы ввели нецелое число.")
            continue
        elif int(input_value) < 0:
            print("Вы ввели отрицательное число.")
            continue
        elif int(input_value) > 255:
            print("Вы ввели число, значение котрого превышает возможности ЦАП.")
            continue
        else:
            GPIO.output(dac, decimal2binary(int(input_value)))
            print("Напряжение на выходе ЦАП (В): {:.3f}".format(int(input_value) * 3.3 / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()