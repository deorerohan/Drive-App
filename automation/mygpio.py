# actual code for controlling GPIO's for RPi will be
# written here
import RPi.GPIO as GPIO
def start():
	GPIO.setmode(GPIO.BOARD)

def setuppin(pin, isout):
	if isout:
		GPIO.setup(pin, GPIO.OUT)
	else:
		GPIO.setup(pin, GPIO.IN)

def toggleswitch(pin):
	GPIO.output(pin, True)


def stop():
	GPIO.cleanup()
