import time
import RPi.GPIO as GPIO
import signalHandler

class Main:
    _pinInputFeederSwitch = 5 # Active LOW!
    _pinInputFilamentRunOutSwitch = 3
    _pinInputPanicAndFireSwitch = 11
    _pinInputSmokeMaintenance = 12

    _pinOutputPwmaFeederMotor = 8
    _pinOutputPwmaLedStrip = 10
    _pinOutputStepperDriverStandby = 13

    _sleepInterval = 0.1

    _feederMotor = None
    _ledStrip = None

    _signalHandler = None


    def __init__(self):
        self._signalHandler = signalHandler.signalHandler()

        # pin numbers as gpio layout
        GPIO.setmode(GPIO.BOARD)

        # configure in / out pins
        GPIO.setup(self._pinInputFeederSwitch, GPIO.IN)
        GPIO.setup(self._pinInputFilamentRunOutSwitch, GPIO.IN)
        GPIO.setup(self._pinInputPanicAndFireSwitch, GPIO.IN)
        GPIO.setup(self._pinInputSmokeMaintenance, GPIO.IN)
        GPIO.setup(self._pinOutputPwmaFeederMotor, GPIO.OUT)
        GPIO.setup(self._pinOutputPwmaLedStrip, GPIO.OUT)
        GPIO.setup(self._pinOutputStepperDriverStandby, GPIO.OUT)

        # init out pins: pwma's low, standby high
        GPIO.output(self._pinOutputPwmaFeederMotor, 0)
        GPIO.output(self._pinOutputPwmaLedStrip, 0)
        GPIO.output(self._pinOutputStepperDriverStandby, 1)

        self._feederMotor = GPIO.PWM(self._pinOutputPwmaFeederMotor, 100)
        self._ledStrip = GPIO.PWM(self._pinOutputPwmaLedStrip, 100)


    def loop(self):
        while True:
            # Clean up and terminate on ctrl-c and sigterm
            if (self._signalHandler.stop):
                GPIO.cleanup()
                break

            # Start / stop feeder motor if switch input is LOW
            if not bool(GPIO.input(self._pinInputFeederSwitch)):
                self._feederMotor.start(80)
            else:
                self._feederMotor.stop()

            time.sleep(self._sleepInterval)


Main().loop()
