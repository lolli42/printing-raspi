import time
import RPi.GPIO as GPIO

PWMA = 8
PWMB = 10
STBY = 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

# init sets led and lego low
GPIO.output(PWMA, 0)
GPIO.output(PWMB, 0)
GPIO.output(STBY, 1)

# lego on for some sec
motor = GPIO.PWM(PWMA, 100)
motor.start(80)
time.sleep(2)
motor.stop()

# led on for some sec
motor = GPIO.PWM(PWMB, 100)
motor.start(80)
time.sleep(2)
motor.stop()

# reset
GPIO.cleanup()
