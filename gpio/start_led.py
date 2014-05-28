import RPi.GPIO as GPIO #import GPIO library
GPIO.setmode(GPIO.BOARD) #use board pin numbering
GPIO.setup(7, GPIO.OUT) #setup gpio pin 7 to out
GPIO.output(7, True) #turn on GPIO pin 7
print("LED started")
GPIO.cleanup()
# www.thirdeyevis.com\pi-page-2.php
# 
