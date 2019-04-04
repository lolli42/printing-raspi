import time
import RPi.GPIO as GPIO

PWMB = 10
STBY = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

GPIO.output(STBY, 1)

light = GPIO.PWM(PWMB, 100)
light.start(100)
time.sleep(0.1)

open('/home/pi/printing-raspi/fauxmo/printer-light-is-on.txt', 'w').close()
