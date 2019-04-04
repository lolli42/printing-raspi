import os
import time
import RPi.GPIO as GPIO

PWMB = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(PWMB, GPIO.OUT)

light = GPIO.PWM(PWMB, 100)
light.start(100)
light.ChangeDutyCycle(0)


if os.path.exists('/home/pi/printing-raspi/fauxmo/printer-light-is-on.txt'):
    os.remove('/home/pi/printing-raspi/fauxmo/printer-light-is-on.txt')
