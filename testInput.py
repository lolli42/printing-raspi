import RPi.GPIO as GPIO

feederSwitch = 5
filamentRunOutSwitch = 3
smokeDetection = 11
smokeMaintenance = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(feederSwitch, GPIO.IN)
GPIO.setup(filamentRunOutSwitch, GPIO.IN)
GPIO.setup(smokeDetection, GPIO.IN)
GPIO.setup(smokeMaintenance, GPIO.IN)

print 'Feeder switch: ' + str(GPIO.input(feederSwitch))
print 'Filament run out switch: ' + str(GPIO.input(filamentRunOutSwitch))
print 'Smoke detection switch: ' + str(GPIO.input(smokeDetection))
print 'Smoke maintenance switch: ' + str(GPIO.input(smokeMaintenance))
