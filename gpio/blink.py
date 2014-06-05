import RPi.GPIO as GPIO # import GPIO library
import time #importtime library. allows us to use sleep

GPIO.setmode(GPIO.BOARD) # use board pin numbering
GPIO.setup(3, GPIO.OUT) # setup GPIO pin 7 to out

# define a function name blink
def Blink(numTimes,speed):
	for i in range(0,numTimes): #run loop numTimes
		print "Iteration " + str(i+1) # print current loop
		GPIO.output(3,True) # switch on pin 7
		time.sleep(speed) # wait for it
		GPIO.output(3,False) # switch off pin 7
		time.sleep(speed) # Legendary
	print "Done" # When loop is complete, print done
	GPIO.cleanup()
# Ask user for total number of blinkes and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

# start blink function. convert user input 
# from strings to numeric data types and pass to Blink as parameters
Blink(int(iterations), float(speed))
